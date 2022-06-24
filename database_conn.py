from models import connect_db, User, Button
from telebot import types


def user_exist(telegram_id):
    database = connect_db()

    if database.query(User).filter(User.telegram_id == telegram_id).one_or_none():
        return True
    return False


def create_user(telegram_id, first_name, last_name, username):
    database = connect_db()

    new_user = User(
        telegram_id=telegram_id,
        first_name=first_name,
        last_name=last_name,
        username=username,
        count_of_pressed_buttons=0
    )

    database.add(new_user)
    database.commit()


def update_user_count_of_pressed_buttons(telegram_id):
    database = connect_db()

    database.query(User).filter(User.telegram_id == telegram_id).update(
        {User.count_of_pressed_buttons: User.count_of_pressed_buttons + 1})
    database.commit()


def button_exist(button_name):
    database = connect_db()

    if database.query(Button).filter(Button.name == button_name).one_or_none():
        return True
    return False


def create_button(button_name):
    database = connect_db()

    new_button = Button(
        name=button_name,
        pressed_count=0
    )

    database.add(new_button)
    database.commit()


def update_pressed_count_of_button(button_name):
    database = connect_db()

    database.query(Button).filter(Button.name == button_name).update({Button.pressed_count: Button.pressed_count + 1})
    database.commit()


def update_pressed_buttons(call: types.CallbackQuery):
    if not button_exist(call.data):
        create_button(call.data)

    update_pressed_count_of_button(call.data)

    if not user_exist(call.from_user.id):
        create_user(call.from_user.id, call.from_user.first_name, call.from_user.last_name,
                    call.from_user.username)

    update_user_count_of_pressed_buttons(call.from_user.id)


def update_main_menu_buttons(message):

    if type(message) is types.Message:

        if not button_exist(message.text):
            create_button(message.text)

        update_pressed_count_of_button(message.text)

        update_user_count_of_pressed_buttons(message.from_user.id)

    if type(message) is types.CallbackQuery:

        if not button_exist(message.data):
            create_button(message.data)

        update_pressed_count_of_button(message.data)

        update_user_count_of_pressed_buttons(message.from_user.id)


def get_users():
    database = connect_db()

    response = [{'telegram_id': user.telegram_id, 'first_name': user.first_name,
                 'last_name': user.last_name, 'username': user.username,
                 'Количество нажатых кнопок': user.count_of_pressed_buttons,
                 'Дата регистрации': user.created_at[:-7]} for user in database.query(User).all()]

    return response


def get_buttons():
    database = connect_db()

    response = [{'Название кнопки': button.name,
                 'Количество нажатий': button.pressed_count} for button in database.query(Button).all()]

    return response


def get_users_ids():
    database = connect_db()

    users = get_users()

    users_ids = [user['telegram_id'] for user in users]

    return users_ids





