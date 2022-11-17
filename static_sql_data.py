# import pandas as pd
from sql import connect_to_sql
import finnhub
from sql_defines import insert_into, values
import json


def insert_command(table_name: str, id_name: str, name: str):
    return f"{insert_into} [Stock_market].[dbo].[{table_name}] ([{id_name}], [{name}])" + values + " ('{}', '{}')"


def add_json_data(cursor, file_name: str, command: str):
    with open(f'static_data/{file_name}', encoding='utf-8') as f:
        data = json.load(f)
        for key in data:
            if isinstance(data[key], list):
                for value in set(data[key]):
                    cursor.execute(command.format(key, value))
            else:
                cursor.execute(command.format(key, data[key]))
        cursor.commit()


def get_symbols(exchange: str, new_file_name: str):
    finnhub_client = finnhub.Client(api_key="canskh2ad3i28ncvae8g")
    data = finnhub_client.stock_symbols(f'{exchange}')
    new_data = {}
    for value in data:
        for key in value:
            if value['currency'] == '':
                value['currency'] = 'None'
            if value['type'] == '':
                value['type'] = 'None'
            if key == "symbol":
                new_data[value["symbol"]] = {"currency": value["currency"],
                                             "type": value["type"]}
    with open(f'static_data/{new_file_name}', 'w+') as new:
        json.dump(new_data, new)
