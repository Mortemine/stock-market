import pyodbc
from datetime import datetime


class Mssql:
    def __init__(self, database, server=r"DESKTOP-4ELEU3H\ALEXEY"):
        self.cnxn = pyodbc.connect("Driver={ODBC Driver 18 for SQL Server};"
                                   "Server="+server+";"
                                   "Database="+database+";"
                                   "Trusted_Connection=yes;"
                                   "TrustServerCertificate=Yes"
                                   )
        self.query = "-- {}\n\n-- Made in Python".format(datetime.now().strftime("%d/%m/%Y"))


def execute_sql(cursor, command):
    try:
        cursor.execute(command)
    except Exception as error:
        return 'error'
    return cursor.fetchone()


def execute_all(cursor, command):
    try:
        cursor.execute(command)
    except Exception as error:
        return 'error'
    return cursor.fetchall()


def execute_sql_update(cursor, command):
    try:
        cursor.execute(command)
    except Exception as error:
        print('error')

    return 'success'


def get_user_id(cursor, values):
    return execute_sql(cursor, 'select [id_пользователя] '
                               'from Пользователи'
                               'where (Логин = "{}" and Пароль = "{}")'
                       .format(values[0], values[1]))


def get_user_info(cursor, user_id):
    return execute_sql(cursor, 'SELECT [Фамилия], [Имя], [Отчество], [дата_рождения]'
                               'FROM [Пользователи]'
                               'WHERE [id_пользователя = "{}"]'.format(user_id))


def get_user_contact_info(cursor, user_id):
    return execute_sql(cursor, 'SELECT [номер_телефона], [mail]'
                               'FROM [Пользователи]'
                               'WHERE [id_пользователя = "{}"]'.format(user_id))


def get_stock_info(cursor):
    return execute_sql(cursor, 'SELECT *'
                               'FROM Сделки')


def get_stock_market_trades(cursor, market_id):
    return execute_sql(cursor, 'SELECT *'
                               'FROM Сделки'
                               'WHERE [биржа] = {}'.format(market_id))


def get_broker_info(cursor, broker_id):
    return execute_sql(cursor, 'SELECT *'
                               'FROM Брокеры'
                               'WHERE [Код_брокера] = {}'.format(broker_id))


def get_instrument_info(cursor, instrument_id):
    return execute_sql(cursor, 'SELECT *'
                               'FROM Инструменты'
                               'WHERE [Код_инструмента] = {}'.format(instrument_id))


def get_instrument_trade_info(cursor, instrument_id):
    return execute_sql(cursor, 'SELECT *'
                               'FROM Котировки'
                               'WHERE [Инструмент] = {}'.format(instrument_id))


mssql_database = Mssql('Stock_market')
crsr = mssql_database.cnxn.cursor()
crsr.execute('INSERT INTO Валюты(Код_валюты, Название) VALUES(?, ?)', 'EUR', 'Евро')
#execute_sql(crsr, 'INSERT INTO Валюты(Код_валюты, Название) VALUES("EUR", "Евро")')
crsr.commit()


