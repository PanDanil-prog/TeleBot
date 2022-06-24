import pandas as pd
import os
from database_conn import get_buttons, get_users
from config import buttons_names


def check_button_exist_in_list(button_name):
    if button_name in buttons_names.keys():
        return buttons_names[button_name]
    else:
        return button_name


def get_buttons_excel():
    if not os.path.exists('report_buttons.xlsx'):
        with open('report_buttons.xlsx', 'w') as users_file:
            pass

    buttons = get_buttons()

    df = pd.DataFrame({'Название кнопки': check_button_exist_in_list(button['Название кнопки']),
                      'Количество нажатий': button['Количество нажатий']} for button in
                        sorted(buttons, key=lambda d: d['Количество нажатий'], reverse=True))

    df.to_excel('./report_buttons.xlsx', sheet_name='Кнопки')


def get_users_excel():
    if not os.path.exists('report_users.xlsx'):
        with open('report_users.xlsx', 'w') as users_file:
            pass

    users = get_users()

    df = pd.DataFrame({'Телеграм ID': user['telegram_id'], 'Имя': user['first_name'],
                       'Фамилия': user['last_name'], 'Username': user['username'],
                       'Количество нажатых кнопок': user['Количество нажатых кнопок'],
                       'Дата регистрации': user['Дата регистрации']} for user in
                        sorted(users, key=lambda d: d['Количество нажатых кнопок'], reverse=True))

    df.to_excel('./report_users.xlsx', sheet_name='Пользователи')

