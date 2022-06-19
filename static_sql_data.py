# import pandas as pd
# from sql import connect_to_sql
import json


def add_countries(cursor):
    with open('static_data/countries.json') as f:
        countries = json.load(f)
        insert_command = "INSERT INTO [Stock_market].[dbo].[Страны] ([Код_страны], [Название]) VALUES('{}', '{}')"
        for key in countries:
            cursor.execute(insert_command.format(key, countries[key]))
        cursor.commit()


def add_cities(cursor):
    with open('static_data/cities.json') as f:
        cities = json.load(f)
        insert_command = "INSERT INTO [Stock_market].[dbo].[Города] ([Наименование], [Страна])" \
                         " VALUES('{}', '{}')"
        for key in cities:
            for value in set(cities[key]):
                cursor.execute(insert_command.format(value, key))
        cursor.commit()


def add_currencies(cursor):
    with open('static_data/currencies.json') as f:
        currencies = json.load(f)
        insert_command = "INSERT INTO [Stock_market].[dbo].[Валюты] ([Код_валюты], [Название]) " \
                         "VALUES ('{}', '{}')"
        for key in currencies:
            print(insert_command.format(key, currencies[key]))
            cursor.execute(insert_command.format(key, currencies[key]))
        cursor.commit()

