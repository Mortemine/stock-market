import PySimpleGUI as sg
import user_interface as ui
import sql


def login_loop(cursor):
    current_window = ui.login_window()

    while True:
        event, values = current_window.read()

        if event == sg.WIN_CLOSED or event == 'Выход':
            current_window.close()
            return 'quit'

        elif event == 'Войти':
            user_id = sql.get_user_id(cursor, values)

            if user_id is None:
                sg.popup_ok('Неправильный логин или пароль.')
            elif user_id == 'error':
                sg.popup_ok('Ошибка запроса к базе данных.')
            else:
                current_window.close()
                return 'work_window' + str(user_id[0])

        if event == 'Регистрация':
            current_window.close()
            return 'register_window'


def registration_loop(cursor):
    current_window = ui.register_window()

    while True:
        event, values = current_window.read()

        if event == sg.WIN_CLOSED or event == 'Выход':
            current_window.close()
            return 'quit'

        elif event == 'Зарегистрироваться':
            if values[7] == values[8]:
                result = sql.register_user(cursor, values)

                if result == 'error':
                    sg.popup_ok('Логин уже занят')
                else:
                    current_window.close()
                    return 'work_window' + str(result[0])
            else:
                sg.popup_ok('Пароли не совпадают')

        elif event == 'Назад':
            current_window.close()
            return 'login_window'


def work_window_loop(cursor, user_id):
    current_window = ui.user_window(cursor, user_id,
                                    ['код_сделки', 'вид_сделки', 'Тикер', 'Количество',
                                     'Биржа', 'Дата'], sql.get_all_trades(cursor),
                                    'Сделки')

    while True:
        event, values = current_window.read()

        if event == sg.WIN_CLOSED:
            current_window.close()
            return 'quit'

        elif event == 'Сделки':
            current_window.close()

            current_window = ui.user_window(cursor, user_id,
                                            ['код_сделки', 'вид_сделки', 'тикер',
                                             'количество', 'биржа', 'дата'],
                                            sql.get_all_trades(cursor), 'Сделки')

        elif event == 'Сделки по биржам':
            current_window.close()
            current_window = ui.user_window(cursor, user_id,
                                            ['код_сделки', 'вид_сделки', 'Тикер', 'Количество',
                                             'Биржа', 'Дата'], sql.get_trades_by_market(cursor, user_id),
                                            'Сделки')

        elif event == 'Биржи':
            current_window.close()
            current_window = ui.user_window(cursor, user_id, ['Код_биржи', 'Название', 'Валюта_торгов'],
                                            sql.get_stock_info(cursor, user_id), 'Биржи')

        elif event == 'Котировки':
            current_window.close()
            current_window = ui.user_window(cursor, user_id,
                                            ['код_котировки', 'цена', 'volume', 'валюта', 'дата', 'владелец', 'тип'],
                                            sql.get_symbol_info(cursor, user_id),
                                            'Котировки')

        elif event == 'Сделки по котировкам':
            current_window.close()
            current_window = ui.user_window(cursor, user_id,
                                            ['код_сделки', 'вид_сделки', 'Тикер', 'Количество',
                                             'Биржа', 'Дата'],
                                            sql.get_trades_by_insrument(cursor, user_id),
                                            'Сделки')

        elif event == 'Выход':
            current_window.close()
            return 'login_window'


def execute():
    sg.theme('DarkGrey13')
    cursor = sql.connect_to_sql()
    result = login_loop(cursor)

    while True:
        if result == 'login_window':
            result = login_loop(cursor)
        if result == 'register_window':
            result = registration_loop(cursor)
        elif result[:11] == 'work_window':
            result = work_window_loop(cursor, result[11:])
        elif result == 'quit':
            break


if __name__ == '__main__':
    execute()
