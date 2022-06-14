import pyodbc
import PySimpleGUI as sg


# noinspection PyBroadException
def connect_to_sql():
    try:
        conn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};' +
                              r'SERVER=DESKTOP-4ELEU3H\ALEXEY;' +
                              'DATABASE=Stock_market;' +
                              'Trusted_Connection=yes;'
                              'TrustServerCertificate=Yes')
    except Exception as error:
        print(error)
        return 'error'

    return conn.cursor()


# noinspection PyBroadException
def execute_sql(cursor, command):
    try:
        cursor.execute(command)
    except Exception as error:
        print(error)
        return 'error'
    return cursor.fetchone()


# noinspection PyBroadException
def execute_all(cursor, commands):
    try:
        cursor.execute(commands)
    except Exception as error:
        print(error)
        return 'error'
    return cursor.fetchall()


# noinspection PyBroadException
def execute_sql_update(cursor, command):
    try:
        cursor.execute(command)
    except Exception as error:
        print(error)
        print('error')

    return 'success'


def get_user_id(cursor, values):
    command = "select [id_пользователя] " + "from [Авторизация] " + \
              "where (Логин = '{}' and Пароль = '{}')".format(values[0], values[1])
    return execute_sql(cursor, command)


def get_user_info(cursor, user_id):
    return execute_sql(cursor, "SELECT [Фамилия], [Имя], [Отчество], [дата_рождения] " 
                               "FROM [Пользователи]"
                               " WHERE [id_пользователя] = {}".format(user_id))


def get_user_contact_info(cursor, user_id):
    return execute_sql(cursor, 'SELECT [номер_телефона], [mail]'
                               'FROM [Пользователи]'
                               'WHERE [id_пользователя] = {}'.format(user_id))


def get_all_trades(cursor):
    return execute_sql(cursor, "SELECT * "
                               "FROM Сделки")


def get_trades_by_market(cursor, market_id):
    return execute_sql(cursor, "SELECT * "
                               "FROM Сделки "
                               "WHERE [биржа] = {}".format(market_id))


def get_broker_info(cursor, broker_id):
    return execute_sql(cursor, "SELECT * "
                               "FROM Брокеры "
                               "WHERE [Код_брокера] = {}".format(broker_id))


def get_instrument_info(cursor, instrument_id):
    return execute_sql(cursor, "SELECT * "
                               "FROM Инструменты "
                               "WHERE [Код_инструмента] = {}".format(instrument_id))


def get_trades_by_insrument(cursor, instrument_id):
    return execute_sql(cursor, "SELECT * "
                               "FROM Котировки "
                               "WHERE [Инструмент] = {}".format(instrument_id))


def get_last_user_id(cursor):
    return execute_sql(cursor, "select max([id_пользователя])"
                               "from [Пользователи]")


def get_all_logins(cursor):
    return execute_all(cursor, "select [Логин] from [Авторизация]")


def register_user(cursor, values):
    new_user_id = int(get_last_user_id(cursor)[0]) + 1
    result = list(map(lambda i: list(i), get_all_logins(cursor)))
    userdata_command = "insert into [Пользователи] " \
                       "([id_пользователя], [Фамилия], [Имя], " \
                       "[Отчество], [дата_рождения], " \
                       "[номер_телефона], [mail]) " \
                       "values ({}, '{}', '{}', '{}', '{}', '{}', '{}')".format(new_user_id,
                                                                                values[0],
                                                                                values[1],
                                                                                values[2],
                                                                                values[3],
                                                                                values[4],
                                                                                values[5])
    login_command = " insert into [dbo].[Авторизация] ([id_пользователя], [Логин], [Пароль])" \
                    " values ({}, '{}', '{}')".format(new_user_id, values[6], values[7])

    if [values[6]] in result:
        return 'error'
    return new_user_id, cursor.execute(userdata_command + login_command).commit()


'''
mssql_database = Mssql('Stock_market')
crsr = mssql_database.cnxn.cursor()
crsr.execute('INSERT INTO Валюты(Код_валюты, Название) VALUES(?, ?)', 'EUR', 'Евро')
# execute_sql(crsr, 'INSERT INTO Валюты(Код_валюты, Название) VALUES("EUR", "Евро")')
crsr.commit()
'''