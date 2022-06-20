# import pandas as pd
# from sql import connect_to_sql
from sql_defines import insert_into, values
import json


def insert_command(table_name, id_name, name):
    return f"{insert_into} [Stock_market].[dbo].[{table_name}] ([{id_name}], [{name}])" + values + " ('{}', '{}')"


def add_json_data(cursor, file_name: str, command):
    with open(f'static_data/{file_name}', encoding='utf-8') as f:
        data = json.load(f)
        for key in data:
            if isinstance(data[key], list):
                for value in set(data[key]):
                    cursor.execute(command.format(key, value))
            else:
                cursor.execute(command.format(key, data[key]))
        cursor.commit()
