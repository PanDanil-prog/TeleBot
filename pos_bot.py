from datetime import datetime
from telebot import TeleBot, types
from config import *
import os.path

bot = TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def welcome_message(message):
    bot.send_message(message.from_user.id, 'Привет, я Бот Бочанский! 👋', reply_markup=kb.welcome_m_up)


@bot.message_handler(commands=['rm'])
def remove_keyboard(message):
    bot.send_message(message.from_user.id, 'Убираю все шаблоны клавиатур', reply_markup=types.ReplyKeyboardRemove())


@bot.message_handler(content_types=['text'])
def main_menu(message):
    if type(message) is types.Message:
        if message.text in ['Общежития', 'Стипендии', 'Проекты', 'Заря', 'РЖД - бонус', 'О профсоюзе', 'Контакты']:
            bot.send_message(message.from_user.id, text=dict_mm[message.text][0],
                             reply_markup=dict_mm[message.text][1])
        else:
            bot.send_message(message.from_user.id, 'Я конечно классный, но пока тебя не понимаю',
                             reply_markup=kb.back_to_mm_markup)

    if type(message) is types.CallbackQuery:
        bot.send_message(message.from_user.id, "Выбери интересующую тебя категорию:", reply_markup=kb.main_menu_m_up)


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


# Scholarship callback handler
@bot.callback_query_handler(func=lambda c: c.data and c.data.startswith('scholarship_'))
def scholarship_inline(call: types.CallbackQuery):
    category = call.data.split('_')[1]
    chat_id, message_id = call.message.chat.id, call.message.message_id
    bot.answer_callback_query(call.id)

    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=dict_scholarship[category][0],
                          reply_markup=dict_scholarship[category][1], parse_mode='Markdown')


# PZD-bonus callback handler
@bot.callback_query_handler(lambda c: c.data and c.data.startswith('rzd_'))
def rzd_inline(call: types.CallbackQuery):
    category = call.data.split('_')[1]
    chat_id, message_id = call.message.chat.id, call.message.message_id
    bot.answer_callback_query(call.id)

    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=dict_rzd[category][0],
                          reply_markup=dict_rzd[category][1])


# Projects callback handler
@bot.callback_query_handler(lambda c: c.data and c.data.startswith('proj_'))
def projects_handler(call: types.CallbackQuery):
    category = call.data.split('_')[1]
    chat_id, message_id = call.message.chat.id, call.message.message_id
    bot.answer_callback_query(call.id)

    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=dict_projects[category][0],
                          reply_markup=dict_projects[category][1])


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


# Return callback
@bot.callback_query_handler(lambda c: c.data and c.data.startswith('return_'))
def return_callback(call: types.CallbackQuery):
    category = call.data.split('_')[1]
    chat_id, message_id = call.message.chat.id, call.message.message_id
    bot.answer_callback_query(call.id)

    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=dict_returns[category][0],
                          reply_markup=dict_returns[category][1])


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
