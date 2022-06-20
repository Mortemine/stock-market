# import pandas as pd
from sql import connect_to_sql
import finnhub
from sql_defines import insert_into, values
import json
import datetime
import random
import time


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


'''main_cursor = connect_to_sql()

with open('static_data/new_us_symbols.json') as f:
    data = json.load(f)
    symbols = [key for key in data]

with open('static_data/stocks.json') as f:
    data = json.load(f)
    stocks = [key for key in data]

while True:
    main_cursor.execute(f"INSERT INTO [Сделки] (вид_сделки, тикер, количество, биржа)"
                        f" VALUES ('trade', '{random.choice(symbols)}', '{random.randint(1,20)}', '{random.choice(stocks)}')")
    time.sleep(1)
    main_cursor.commit()'''
