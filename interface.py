import PySimpleGUI as sg
import mssql_connection as mssql

def login_window():
    layout = [[sg.Text('Логин:', size=(6, 1)), sg.InputText(default_text='admin')],
              [sg.Text('Пароль:', size=(6, 1)), sg.InputText(default_text='admin')],
              [sg.Button('Войти'), sg.Button('Выход'), sg.Button('Регистрация')]
              ]

    return sg.Window('Войти в систему', layout)


def register_window():
    layout = [[sg.Text('Фамилия:', size=(6, 1)), sg.InputText(default_text='')],
              [sg.Text('Имя:', size=(6, 1)), sg.InputText(default_text='')],
              [sg.Text('Отчество:', size=(6, 1)), sg.InputText(default_text='')],
              [sg.Text('Дата рождения:', size=(6, 1)), sg.InputText(default_text='')],
              [sg.Text('Номер телефона:', size=(6, 1)), sg.InputText(default_text='')],
              [sg.Text('E-mail:', size=(6, 1)), sg.InputText(default_text='')],
              [sg.Text('Введите логин:', size=(6, 1)), sg.InputText(default_text='')],
              [sg.Text('Введите пароль:', size=(6, 1)), sg.InputText(default_text='')],
              [sg.Text('Подтвердите пароль:', size=(6, 1)), sg.InputText(default_text='')],
              [sg.Button('Зарегистрироваться'), sg.Button('Назад'), sg.Button('Выход')]
              ]

    return sg.Window('Войти в систему', layout)


def user_window(cursor, user_id, headings, data, tooltip):
    user_info = mssql.get_user_info(cursor, user_id)  # [Фамилия], [Имя], [Отчество], [дата_рождения]'

    user_contact_info = mssql.get_user_contact_info(cursor, user_id)

    data = list(map(lambda i:list(i), data))

    layout = [[sg.Text('{} {} {} {}'.format(user_info[0], user_info[1], user_info[2], user_info[3])],
              [sg.Button('')]
             ]
