from datetime import datetime

from telebot import TeleBot, types

from config import *
from info import media_pos
from utils import get_buttons_excel, get_users_excel

import os.path

from database_conn import user_exist, create_user, update_pressed_buttons, update_main_menu_buttons, get_users_ids

bot = TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def welcome_message(message):
    if not user_exist(message.from_user.id):
        create_user(message.from_user.id, message.from_user.first_name, message.from_user.last_name,
                    message.from_user.username)

    bot.send_message(message.from_user.id, '''Привет 👋\n\nЯ чат - бот Профсоюзной Организации Студентов ННГУ''',
                     reply_markup=kb.welcome_m_up)


@bot.message_handler(commands=['report'])
def report_message(message: types.Message):
    if message.from_user.id in [842533153, 288708117]:
        bot.send_message(message.from_user.id, text='Ой, да ты у нас администратор, жмяу на кнопку, которая тебе нужна',
                         reply_markup=kb.report_markup)
    else:
        bot.send_message(message.from_user.id, text='У вас нет прав для доступа к этой команде')


@bot.message_handler(commands=['send_all'])
def send_messages_to_all(message: types.Message):
    sender_id = message.from_user.id
    if message.from_user.id in [842533153, 288708117]:
        users_ids = get_users_ids()

        for id in users_ids:
            try:
                bot.send_message(id, 'Не пугайтесь, это тестовая рассылка!\nСпасибо, что помогаете тестировать бота❤')
            except Exception as err:
                bot.send_message(sender_id, f'Ошибка при отправке сообщения пользователю с id: {id}')

    else:
        bot.send_message(message.from_user.id, 'У вас нет прав для доступа к этой команде')


@bot.message_handler(content_types=['text'])
def main_menu(message):
    if type(message) is types.Message:
        if message.text in ['Общежития', 'Стипендии', 'Проекты', 'Заря', 'РЖД - бонус', 'О профсоюзе', 'Контакты']:
            bot.send_message(message.from_user.id, text=dict_mm[message.text][0],
                             reply_markup=dict_mm[message.text][1], parse_mode='Markdown')
            update_main_menu_buttons(message)

        elif message.text == 'Медиа ПОС':
            bot.send_message(message.from_user.id, text=media_pos, disable_web_page_preview=True, parse_mode='Markdown')
            update_main_menu_buttons(message)

        else:
            response_message = '''Я всего лишь бот и пока не понимаю тебя.\n\nЕсли ты потерялся, то нажми кнопку ниже👇
Или нажми на команду /start'''
            bot.send_message(message.from_user.id, response_message,
                             reply_markup=kb.back_to_mm_markup)

    if type(message) is types.CallbackQuery:
        bot.send_message(message.from_user.id, "Выбери интересующую тебя категорию:", reply_markup=kb.main_menu_m_up)
        update_main_menu_buttons(message)

    if not user_exist(message.from_user.id):
        create_user(message.from_user.id, message.from_user.first_name, message.from_user.last_name,
                    message.from_user.username)


# Start callback
@bot.callback_query_handler(func=lambda c: c.data == 'welcome_message' or c.data == 'return_to_mm')
def process_callback_welcome(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    main_menu(callback_query)


# Dorm callback handler
@bot.callback_query_handler(func=lambda c: c.data and c.data.startswith('dorm_'))
def dorm_inline(call: types.CallbackQuery):
    category = call.data.split('_')[1]
    chat_id, message_id = call.message.chat.id, call.message.message_id
    bot.answer_callback_query(call.id)

    if category == 'summer-docs':
        bot.send_document(chat_id, open('docs/Zayavlenie_leto.doc', 'rb'))
    else:
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=dict_dorm[category][0],
                              reply_markup=dict_dorm[category][1])

    update_pressed_buttons(call)


# Scholarship callback handler
@bot.callback_query_handler(func=lambda c: c.data and c.data.startswith('scholarship_'))
def scholarship_inline(call: types.CallbackQuery):
    category = call.data.split('_')[1]
    chat_id, message_id = call.message.chat.id, call.message.message_id
    bot.answer_callback_query(call.id)

    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=dict_scholarship[category][0],
                          reply_markup=dict_scholarship[category][1], parse_mode='Markdown')

    update_pressed_buttons(call)


# PZD-bonus callback handler
@bot.callback_query_handler(lambda c: c.data and c.data.startswith('rzd_'))
def rzd_inline(call: types.CallbackQuery):
    category = call.data.split('_')[1]
    chat_id, message_id = call.message.chat.id, call.message.message_id
    bot.answer_callback_query(call.id)

    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=dict_rzd[category][0],
                          reply_markup=dict_rzd[category][1])

    update_pressed_buttons(call)


# Projects callback handler
@bot.callback_query_handler(lambda c: c.data and c.data.startswith('proj_'))
def projects_handler(call: types.CallbackQuery):
    category = call.data.split('_')[1]
    chat_id, message_id = call.message.chat.id, call.message.message_id
    bot.answer_callback_query(call.id)

    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=dict_projects[category][0],
                          reply_markup=dict_projects[category][1])

    update_pressed_buttons(call)


# SSOL callback handler
@bot.callback_query_handler(lambda c: c.data and c.data.startswith('ssol_'))
def ssol_handler(call: types.CallbackQuery):
    category = call.data.split('_')[1]
    chat_id, message_id = call.message.chat.id, call.message.message_id
    bot.answer_callback_query(call.id)

    if category == 'process-docs-take':
        bot.send_document(chat_id, open('docs/Zayavlenie_v_SSOL_Zarya.docx', 'rb'))
    else:
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=dict_ssol[category][0],
                              reply_markup=dict_ssol[category][1])

    update_pressed_buttons(call)


# Contacts callback handler
@bot.callback_query_handler(lambda c: c.data and c.data.startswith('contacts_'))
def contacts_handler(call: types.CallbackQuery):
    category = call.data.split('_')[1]
    chat_id, message_id = call.message.chat.id, call.message.message_id
    bot.answer_callback_query(call.id)

    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=dict_contacts[category][0],
                          reply_markup=dict_contacts[category][1], parse_mode='Markdown')

    update_pressed_buttons(call)


# Return callback
@bot.callback_query_handler(lambda c: c.data and c.data.startswith('return_'))
def return_callback(call: types.CallbackQuery):
    category = call.data.split('_')[1]
    chat_id, message_id = call.message.chat.id, call.message.message_id
    bot.answer_callback_query(call.id)

    if category == 'contacts':
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=dict_returns[category][0],
                              reply_markup=dict_returns[category][1], parse_mode='Markdown')
    else:
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=dict_returns[category][0],
                              reply_markup=dict_returns[category][1])


# Report handler
@bot.callback_query_handler(lambda c: c.data and c.data.startswith('report_'))
def report_callback(call: types.CallbackQuery):
    category = call.data.split('_')[1]
    chat_id, message_id = call.message.chat.id, call.message.message_id
    bot.answer_callback_query(call.id)

    if category == 'users':
        get_users_excel()

        bot.send_document(chat_id=chat_id, document=open('./report_users.xlsx', 'rb'))

    if category == 'buttons':
        get_buttons_excel()

        bot.send_document(chat_id=chat_id, document=open('./report_buttons.xlsx', 'rb'))


while True:
    try:
        bot.polling(none_stop=True, interval=0)
    except Exception as e:
        if not os.path.exists('errors.txt'):
            with open('errors.txt', 'w') as file:
                file.write(f'{str(datetime.now())[:-7]} | Exception is: {str(e)}\n\n')
        else:
            with open('errors.txt', 'a+') as file:
                file.write(f'{str(datetime.now())[:-7]} | Exception is: {str(e)}\n\n')
