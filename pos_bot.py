from datetime import datetime

from telebot import TeleBot, types

from config import *
from info import media_pos
from utils import get_buttons_excel, get_users_excel
import keyboards as kb

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


@bot.message_handler(commands=['admin'])
def admin_menu(message: types.Message):
    sender_id = message.from_user.id

    if sender_id in [842533153, 288708117]:
        bot.send_message(chat_id=sender_id, text='Меню администратора, выбирай, что тебе нужно сделать',
                         reply_markup=kb.admin_main_markup)
    else:
        bot.send_message(sender_id, 'Access denied')


@bot.message_handler(content_types=['text'])
def main_menu(message):
    if type(message) is types.Message:
        if message.text in ['Общежития 🏡', 'Стипендии 💰', 'Проекты 🔥', 'Заря 🌳', 'РЖД - бонус 🎁', 'О профсоюзе 🏠',
                            'Контакты ☎']:
            bot.send_message(message.from_user.id, text=dict_mm[message.text][0],
                             reply_markup=dict_mm[message.text][1], parse_mode='Markdown')
            update_main_menu_buttons(message)

        elif message.text == 'Медиа ПОС 🔗':
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
        bot.send_document(chat_id, open('docs/Заявление Старшекурсники Лето.doc', 'rb'))
    elif category == 'enrolle-docs-take':
        bot.send_document(chat_id, open('docs/Заявление абитуриенты.doc', 'rb'))
        bot.send_document(chat_id, open('docs/Льготные Категории.pdf', 'rb'))
    else:
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=dict_dorm[category][0],
                              reply_markup=dict_dorm[category][1], parse_mode='Markdown')

    update_pressed_buttons(call)


# Scholarship callback handler
@bot.callback_query_handler(func=lambda c: c.data and c.data.startswith('scholarship_'))
def scholarship_inline(call: types.CallbackQuery):
    category = call.data.split('_')[1]
    chat_id, message_id = call.message.chat.id, call.message.message_id
    bot.answer_callback_query(call.id)

    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=dict_scholarship[category][0],
                          reply_markup=dict_scholarship[category][1], parse_mode='Markdown',
                          disable_web_page_preview=True)

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
        bot.send_document(chat_id, open('docs/Заявление в ССОЛ Заря.docx', 'rb'))
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

    if category == 'contacts' or category == 'dorm-enrolle':
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=dict_returns[category][0],
                              reply_markup=dict_returns[category][1], parse_mode='Markdown')
    else:
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=dict_returns[category][0],
                              reply_markup=dict_returns[category][1])


# Admin handler
@bot.callback_query_handler(lambda c: c.data and c.data.startswith('admin_'))
def report_callback(call: types.CallbackQuery):
    category = call.data.split('_')[1]
    chat_id, message_id = call.message.chat.id, call.message.message_id
    bot.answer_callback_query(call.id)
    sender_id = call.from_user.id

    if sender_id in [842533153, 288708117]:

        if category == 'send-all':
            bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                  text=info.admin_send,
                                  reply_markup=kb.admin_send_all_markup,
                                  parse_mode='Markdown')

        if category == 'send-all-send':
            msg = bot.send_message(chat_id=chat_id,
                                   text='''Напиши да или yes если ты уверен, что хочешь отправить сообщение всем пользователям
В противном случае напиши что угодно, кроме да/yes''')

            bot.register_next_step_handler(msg, confirm_send_message)

        if category == 'send-all-edit':

            if os.path.exists('upload_image.jpg'):
                path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'upload_image.jpg')
                os.remove(path)

            msg = bot.send_message(chat_id=chat_id, text='--- Редактирование сообщения ---\n\nВведи текст:')

            bot.register_next_step_handler(msg, create_text_for_send_message)

        if category == 'send-all-view':

            if os.path.exists('text_for_send_message.md'):

                with open('text_for_send_message.md', 'r') as f:
                    text = f.read()

                if text is None:
                    bot.send_message(sender_id, 'Файл с текстом пустой, отредактируй его в кнопке "Редактировать"')
                else:
                    bot.send_message(sender_id, text, parse_mode='Markdown')

            if os.path.exists('upload_image.jpg'):
                bot.send_photo(sender_id, open('upload_image.jpg', 'rb'))

        if category == 'report':
            bot.edit_message_text(chat_id=chat_id, message_id=message_id, text='Выбери нужный тебе отчет',
                                  reply_markup=kb.admin_report_markup)

        if category == 'report-users':
            get_users_excel()

            bot.send_document(chat_id=chat_id, document=open('./report_users.xlsx', 'rb'))

        if category == 'report-buttons':
            get_buttons_excel()

            bot.send_document(chat_id=chat_id, document=open('./report_buttons.xlsx', 'rb'))

    else:
        bot.send_message(sender_id, text='Access denied')


def confirm_get_photo_from_admin(message: types.Message):
    sender_id = message.from_user.id

    if sender_id in [842533153, 288708117]:

        if message.text.lower() in ['да', 'yes']:

            msg = bot.send_message(sender_id, 'Скинь сюда фотографию, которая нужна')
            bot.register_next_step_handler(msg, get_photo_from_admin)

        else:
            bot.send_message(sender_id, 'Хорошо, обойдемся без фотографии')

    else:
        bot.send_message(sender_id, 'Access denied')


def get_photo_from_admin(message: types.Message):
    sender_id = message.from_user.id

    if sender_id in [842533153, 288708117]:

        try:

            file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
            downloaded_file = bot.download_file(file_info.file_path)

            src = os.path.dirname(__file__) + r'\upload_image.' + file_info.file_path.split('.')[1]

            with open(src, 'wb') as new_file:
                new_file.write(downloaded_file)
                bot.send_message(sender_id, 'Фотография успешно сохранена')

        except Exception as e:
            bot.send_message(sender_id, f'Что то пошло не так - ошибка: {e}')

    else:

        bot.send_message(sender_id, 'Access denied')


def confirm_send_message(message: types.Message):
    sender_id = message.from_user.id

    if sender_id in [842533153, 288708117]:

        if message.text.lower() in ['yes', 'да']:
            users_ids = get_users_ids()

            if os.path.exists('text_for_send_message.md'):

                with open('text_for_send_message.md', 'r') as text_file:
                    text = text_file.read()

                for id in users_ids:

                    try:

                        bot.send_message(sender_id, text=text, parse_mode='Markdown')

                        if os.path.exists('upload_image.jpg'):
                            bot.send_photo(sender_id, open('upload_image.jpg', 'rb'))

                    except Exception as e:

                        bot.send_message(sender_id, f'Ошибка при отправке сообщения пользователю с id: {id}')

            else:
                bot.send_message(sender_id, 'Сначала создай файл в кнопке "Редактировать"')

            bot.send_message(sender_id, 'Сообщение отправлено всем пользователям.')
        else:
            bot.send_message(sender_id, 'Отправка сообщения отменена.\nВозвращаю тебя в меню админа')
            bot.send_message(sender_id, 'Меню администратора, выбирай, что тебе нужно сделать',
                             reply_markup=kb.admin_main_markup)
    else:
        bot.send_message(sender_id, text='Access denied')


def create_text_for_send_message(message: types.Message):
    sender_id = message.from_user.id
    if sender_id in [842533153, 288708117]:
        try:

            with open('text_for_send_message.md', 'w') as text_file:

                text_file.write(message.text)

        except Exception as e:
            bot.send_message(message.from_user.id,
                             f'Произошла ошибка - {e}\n\nВозможно ты ввел символы, которые не может понять программа, например стикеры')

        msg = bot.send_message(sender_id,
                               'Текст сохранен\n\nНужна ли фотография? Введи Да или yes, если нужна, в противном случае введи нет')
        bot.register_next_step_handler(msg, confirm_get_photo_from_admin)

    else:
        bot.send_message(sender_id, text='Access denied')


while True:
    try:
        bot.polling(none_stop=True, interval=0, skip_pending=True)
    except Exception as e:
        if not os.path.exists('errors.txt'):
            with open('errors.txt', 'w') as file:
                file.write(f'{str(datetime.now())[:-7]} | Exception is: {str(e)}\n\n')
        else:
            with open('errors.txt', 'a+') as file:
                file.write(f'{str(datetime.now())[:-7]} | Exception is: {str(e)}\n\n')
