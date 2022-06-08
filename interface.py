import PySimpleGUI as sg


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
