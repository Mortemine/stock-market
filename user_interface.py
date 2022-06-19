import PySimpleGUI as sg
import sql as mssql


def login_window():
    layout = [[sg.Text('Логин:', size=(6, 1)), sg.InputText(default_text='admin')],
              [sg.Text('Пароль:', size=(6, 1)), sg.InputText(default_text='admin')],
              [sg.Button('Войти'), sg.Button('Выход'), sg.Button('Регистрация')]
              ]

    return sg.Window('Войти в систему', layout)


def register_window():
    layout = [[sg.Text('Фамилия:', size=(16, 1)), sg.InputText(default_text='Familia')],
              [sg.Text('Имя:', size=(16, 1)), sg.InputText(default_text='Name')],
              [sg.Text('Отчество:', size=(16, 1)), sg.InputText(default_text='Otchestvo')],
              [sg.Text('Дата рождения:', size=(16, 1)), sg.InputText(default_text='12-12-2000')],
              [sg.Text('Номер телефона:', size=(16, 1)), sg.InputText(default_text='12321425')],
              [sg.Text('E-mail:', size=(16, 1)), sg.InputText(default_text='mail')],
              [sg.Text('Введите логин:', size=(16, 1)), sg.InputText(default_text='login')],
              [sg.Text('Введите пароль:', size=(16, 1)), sg.InputText(default_text='pass')],
              [sg.Text('Подтвердите пароль:', size=(16, 1)), sg.InputText(default_text='pass')],
              [sg.Button('Зарегистрироваться'), sg.Button('Назад'), sg.Button('Выход')]
              ]

    return sg.Window('Регистрация', layout)


def user_window(cursor, user_id, headings, data, tooltip):
    user_info = mssql.get_user_info(cursor, user_id)  # [Фамилия], [Имя], [Отчество], [дата_рождения]'
    # user_contact_info = mssql.get_user_contact_info(cursor, user_id)
    data = list(map(lambda i: list(i), [data]))

    layout = [[sg.Text("{} {} {}".format(user_info[0], user_info[1], user_info[2]),
                       justification='center'), sg.Button('Выход')],
              [sg.Button('Сделки'),
               sg.Button('Сделки по биржам'),
               sg.Button('Брокеры'),
               sg.Button('Инструменты'),
               sg.Button('Котировки')
               ],
              [sg.Table(values=data,
                        visible=True,
                        headings=headings,
                        max_col_width=35,
                        background_color='white',
                        auto_size_columns=True,
                        text_color='black',
                        display_row_numbers=False,
                        justification='right',
                        num_rows=len(data),
                        alternating_row_color='lightgray',
                        key='_Table_',
                        row_height=20,
                        tooltip=tooltip)]
              ]
    return sg.Window('Окно пользователя', layout, size=(854, 480), element_justification='c')
