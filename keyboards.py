from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, \
    KeyboardButton, ReplyKeyboardMarkup

# ----------LINKS----------
insta_url = InlineKeyboardButton(text='Инстаграм', url='https://www.instagram.com/pos_nngu/')
vk_url = InlineKeyboardButton(text='Группа ВК', url='https://vk.com/pos_nngu')

# ----------Back Buttons----------

return_to_dorm_main = InlineKeyboardButton(text='Назад', callback_data='return_dorm-main')
return_to_undergrad = InlineKeyboardButton(text='Назад', callback_data='return_undergrad')
return_to_underdocs = InlineKeyboardButton(text='Назад', callback_data='return_underdocs')
return_to_scholarship_main = InlineKeyboardButton(text='Назад', callback_data='return_scholarship')
return_to_scholarship_gss = InlineKeyboardButton(text='Назад', callback_data='return_gss')
return_to_scholarship_gas = InlineKeyboardButton(text='Назад', callback_data='return_gas')
return_to_rzd_main = InlineKeyboardButton(text='Назад', callback_data='return_rzd')
return_to_ssol_main = InlineKeyboardButton(text='Назад', callback_data='return_ssol')
return_to_ssol_types = InlineKeyboardButton(text='Назад', callback_data='return_types')
return_to_ssol_process = InlineKeyboardButton(text='Назад', callback_data='return_process')
return_to_proj_main = InlineKeyboardButton(text='Назад', callback_data='return_proj')
return_to_dorm_list = InlineKeyboardButton(text='Назад', callback_data='return_dorm-list')
return_to_dorm_summer = InlineKeyboardButton(text='Назад', callback_data='return_dorm-summer')

# ----------END BACK BUTTONS----------

# Return to main menu
back_to_main_menu_btn = InlineKeyboardButton('Вернуться в главное меню', callback_data='return_to_mm')

back_to_mm_markup = InlineKeyboardMarkup().add(back_to_main_menu_btn)

# Welcome button
welcome_button = InlineKeyboardButton('Привет! 👋', callback_data='welcome_message')

welcome_m_up = InlineKeyboardMarkup().add(welcome_button)

# Main Menu
btn1, btn2, btn3, btn4, \
btn5, btn6, btn7 = KeyboardButton('Общежития'), KeyboardButton('Стипендии'), \
                   KeyboardButton('РЖД - бонус'), KeyboardButton('Проекты'), \
                   KeyboardButton('О профсоюзе'), KeyboardButton('Заря'), \
                   KeyboardButton('Контакты')

main_menu_m_up = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(btn1, btn2, btn4, btn6,
                                                                            btn3, btn5)
main_menu_m_up.row(btn7)

# ----------Dormitories----------

# Main menu
in_keyboard_undergrad = InlineKeyboardButton('Старшекурсники', callback_data='dorm_undergrad')
in_keyboard_enrollee = InlineKeyboardButton('Абитуриенты', callback_data='dorm_enrollee')
dorm_list_button = InlineKeyboardButton('Список Общежитий', callback_data='dorm_list')
dorm_summer = InlineKeyboardButton('Старшекурсники Лето', callback_data='dorm_summer')

dorm_keyb_m_up = InlineKeyboardMarkup().add(in_keyboard_undergrad, in_keyboard_enrollee)
dorm_keyb_m_up.row(dorm_summer)
dorm_keyb_m_up.row(dorm_list_button)

# Dorm undergrad
undergrad_inline_keyb = InlineKeyboardButton('📒 Комплект документов', callback_data='dorm_underdocs')
undergrad_keyb_url = InlineKeyboardButton('🗿 Перейти в вк', url='https://vk.com/pos_nngu?w=wall-11163281_13296')

dorm_enrolee_markup = InlineKeyboardMarkup().add(return_to_dorm_main)
dorm_undergrad_keyb_m_up = InlineKeyboardMarkup(row_width=1).add(undergrad_inline_keyb,
                                                                 undergrad_keyb_url, return_to_dorm_main)

# Dorm undergrad docs
under_docs1, under_docs2, under_docs3 = InlineKeyboardButton('Я уже живу в общежитии',
                                                             callback_data='dorm_already-living'), \
                                        InlineKeyboardButton('Я не проживаю в общежитии, но хочу в него заселиться',
                                                             callback_data='dorm_do-not-live'), \
                                        InlineKeyboardButton('Я заканчиваю ВУЗ и планирую поступать в магистратуру',
                                                             callback_data='dorm_master')

dorm_summer_do = InlineKeyboardButton('Что мне надо сделать?', callback_data='dorm_summer-do')
dorm_summer_docs = InlineKeyboardButton('Получить документы', callback_data='dorm_summer-docs')
dorm_summer_url = InlineKeyboardButton('Пост в ВК', url='https://vk.com/pos_nngu?w=wall-11163281_13907')

dorm_underdocs_keyb_m_up = InlineKeyboardMarkup(row_width=1).add(under_docs1, under_docs2,
                                                                 under_docs3, return_to_undergrad)

dorm_summer_markup = InlineKeyboardMarkup(row_width=1).add(dorm_summer_do, dorm_summer_docs,
                                                           dorm_summer_url, return_to_dorm_main)

dorm_summer_do_markup = InlineKeyboardMarkup(row_width=1).add(return_to_dorm_summer)

dorm_return_to_underdocs_markup = InlineKeyboardMarkup().add(return_to_underdocs)

# List of dormitories
dorm_2, dorm_4, dorm_6, \
dorm_7, dorm_8, dorm_9 = InlineKeyboardButton(text='Общежитие 2', callback_data='dorm_2'), \
                         InlineKeyboardButton(text='Общежитие 4', callback_data='dorm_4'), \
                         InlineKeyboardButton(text='Общежитие 6', callback_data='dorm_6'), \
                         InlineKeyboardButton(text='Общежитие 7', callback_data='dorm_7'), \
                         InlineKeyboardButton(text='Общежитие 8', callback_data='dorm_8'), \
                         InlineKeyboardButton(text='Общежитие 9', callback_data='dorm_9')

dorm_2_url, dorm_4_url, dorm_6_url, \
dorm_7_url, dorm_8_url, dorm_9_url = InlineKeyboardButton(text='Группа ВК', url='https://vk.com/sso_2_nngu'), \
                                     InlineKeyboardButton(text='Группа ВК', url='https://vk.com/sso_4_unn'), \
                                     InlineKeyboardButton(text='Группа ВК', url='https://vk.com/unn_sso6'), \
                                     InlineKeyboardButton(text='Группа ВК', url='https://vk.com/obsh7nngu'), \
                                     InlineKeyboardButton(text='Группа ВК', url='https://vk.com/8obsh'), \
                                     InlineKeyboardButton(text='Группа ВК', url='https://vk.com/hostel9unn')

dorm_list_markup = InlineKeyboardMarkup(row_width=1).add(dorm_2, dorm_4, dorm_6, dorm_7,
                                                         dorm_8, dorm_9, return_to_dorm_main)

dorm_2_markup = InlineKeyboardMarkup(row_width=1).add(dorm_2_url, return_to_dorm_list)
dorm_4_markup = InlineKeyboardMarkup(row_width=1).add(dorm_4_url, return_to_dorm_list)
dorm_6_markup = InlineKeyboardMarkup(row_width=1).add(dorm_6_url, return_to_dorm_list)
dorm_7_markup = InlineKeyboardMarkup(row_width=1).add(dorm_7_url, return_to_dorm_list)
dorm_8_markup = InlineKeyboardMarkup(row_width=1).add(dorm_8_url, return_to_dorm_list)
dorm_9_markup = InlineKeyboardMarkup(row_width=1).add(dorm_9_url, return_to_dorm_list)

# ----------END DORMITORIES----------

# ----------Scholarship----------

# Main menu
GAS_button = InlineKeyboardButton('ГАС', callback_data='scholarship_gas')
PGAS_button = InlineKeyboardButton('ПГАС', callback_data='scholarship_pgas')
GSS_button = InlineKeyboardButton('ГСС', callback_data='scholarship_gss')
PGSS_button = InlineKeyboardButton('ПГСС', callback_data='scholarship_pgss')

scholarship_markup = InlineKeyboardMarkup(row_width=2).add(GAS_button, GSS_button, PGAS_button, PGSS_button)

gas_size = InlineKeyboardButton('Размер стипендии', callback_data='scholarship_gas-size')
gas_criteries = InlineKeyboardButton('Критерии получения', callback_data='scholarship_gas-criteries')

gss_size = InlineKeyboardButton('Размер стипендии', callback_data='scholarship_gss-size')
gss_people = InlineKeyboardButton('Кому положена социальная стипендия?', callback_data='scholarship_gss-people')
gss_where = InlineKeyboardButton('Куда подавать', callback_data='scholarship_gss-where')
gss_documents = InlineKeyboardButton('Какие документы нужны', callback_data='scholarship_gss-docs')

gas_markup = InlineKeyboardMarkup(row_width=1).add(gas_size, gas_criteries, return_to_scholarship_main)
gss_markup = InlineKeyboardMarkup(row_width=1).add(gss_size, gss_people, gss_where, gss_documents,
                                                   return_to_scholarship_main)
pgas_markup = InlineKeyboardMarkup().add(return_to_scholarship_main)
pgss_markup = InlineKeyboardMarkup().add(return_to_scholarship_main)

return_to_gss_markup = InlineKeyboardMarkup().add(return_to_scholarship_gss)
return_to_gas_markup = InlineKeyboardMarkup().add(return_to_scholarship_gas)

# ----------END SCHOLARSHIP----------

# ----------RZD BONUS----------

# Main menu
rzd_participant = InlineKeyboardButton('Как стать участником программы', callback_data='rzd_participant')
rzd_timing = InlineKeyboardButton('Сроки действия программы', callback_data='rzd_timing')

rzd_markup = InlineKeyboardMarkup(row_width=1).add(rzd_participant, rzd_timing)
rzd_return_to_main_menu_markup = InlineKeyboardMarkup().add(return_to_rzd_main)

# ----------END RZD BONUS----------

# ----------Projects----------

# Main menu
proj1, proj2, proj3, \
proj4, proj5, proj6, \
proj7, proj8 = InlineKeyboardButton('ДНК', callback_data='proj_dnk'), \
               InlineKeyboardButton('Живая Земля', callback_data='proj_jz'), \
               InlineKeyboardButton('Разумный выбор', callback_data='proj_rv'), \
               InlineKeyboardButton('Сильные Духом', callback_data='proj_sd'), \
               InlineKeyboardButton('Что? Где? Когда?', callback_data='proj_cgk'), \
               InlineKeyboardButton('Конгресс', callback_data='proj_kongress'), \
               InlineKeyboardButton('Брусничный Джем', callback_data='proj_bdj'), \
               InlineKeyboardButton('Конкурс ССО', callback_data='proj_sso')

projects_main_menu_markup = InlineKeyboardMarkup(row_width=2).add(proj1, proj2, proj3, proj4,
                                                                  proj5, proj6, proj7, proj8)

# DNK
proj_dnk_url = InlineKeyboardButton('Группа ВК', url='https://vk.com/dnk_nngu')

proj_dnk_markup = InlineKeyboardMarkup(row_width=1).add(proj_dnk_url, return_to_proj_main)

# Living Earth
proj_jz_url = InlineKeyboardButton('Группа ВК', url='https://vk.com/zhivaya_zemlya')

proj_jz_markup = InlineKeyboardMarkup(row_width=1).add(proj_jz_url, return_to_proj_main)

# Smart choice
proj_rv_url = InlineKeyboardButton('Группа ВК', url='https://vk.com/ssol_zarya_nngu')

proj_rv_markup = InlineKeyboardMarkup(row_width=1).add(proj_rv_url, return_to_proj_main)

# Strong boys
proj_sd_url = InlineKeyboardButton('Группа ВК', url='https://vk.com/silnie_duxom')

proj_sd_markup = InlineKeyboardMarkup(row_width=1).add(proj_sd_url, return_to_proj_main)

# What? Where? When?
proj_cgk_url = InlineKeyboardButton('Группа ВК', url='https://vk.com/intclub_nngu')

proj_cgk_markup = InlineKeyboardMarkup(row_width=1).add(proj_cgk_url, return_to_proj_main)

# Kongress
proj_kongress_url = InlineKeyboardButton('Группа ВК', url='https://vk.com/razumnyyvybor')

proj_kongress_markup = InlineKeyboardMarkup(row_width=1).add(proj_kongress_url, return_to_proj_main)

# Brusnichniy Djem
proj_bdj_url = InlineKeyboardButton('Группа ВК', url='https://vk.com/jam_nnov')

proj_bdj_markup = InlineKeyboardMarkup(row_width=1).add(proj_bdj_url, return_to_proj_main)

# SSO
proj_sso_url = InlineKeyboardButton('Группа ВК', url='https://vk.com/sso_unn')

proj_sso_markup = InlineKeyboardMarkup(row_width=1).add(proj_sso_url, return_to_proj_main)

# ----------END PROJECTS----------

# ----------About POS----------

about_pos_markup = InlineKeyboardMarkup().add(vk_url)

# ----------END ABOUT POS----------

# ----------SSOL ZARYA----------

# Main menu
ssol_types = InlineKeyboardButton(text='Смены', callback_data='ssol_types')
ssol_cost = InlineKeyboardButton(text='Стоимость', callback_data='ssol_cost')
ssol_process = InlineKeyboardButton(text='Процедура приобретения путевки', callback_data='ssol_process')
ssol_quiz = InlineKeyboardButton(text='Розыгрыш путевки', callback_data='ssol_quiz')
ssol_url1 = InlineKeyboardButton(text='Заполнить заявку',
                                 url='https://docs.google.com/forms/d/11kVGuX7I1FYQgYGhUh9FPRCe4loujZW9MKCBi-J5W0U/edit')
ssol_url2 = InlineKeyboardButton(text='Группа ВК', url='https://vk.com/ssol_zarya_nngu')

ssol_main_markup = InlineKeyboardMarkup(row_width=2).add(ssol_types, ssol_cost)
ssol_main_markup.row(ssol_process)
ssol_main_markup.row(ssol_quiz)
ssol_main_markup.row(ssol_url1)
ssol_main_markup.row(ssol_url2)

# ssol types
ssol_types_health = InlineKeyboardButton(text='Отдыхай на здоровье', callback_data='ssol_health')
ssol_types_battle = InlineKeyboardButton(text='Битва Студсоветов', callback_data='ssol_battle')
ssol_types_choice = InlineKeyboardButton(text='Разумный выбор', callback_data='ssol_choice')
ssol_types_creative = InlineKeyboardButton(text='Креативные индустрии', callback_data='ssol_creative')

ssol_types_markup = InlineKeyboardMarkup(row_width=1).add(ssol_types_health, ssol_types_battle,
                                                          ssol_types_choice, ssol_types_creative,
                                                          return_to_ssol_main)

# ssol process

ssol_process_docs = InlineKeyboardButton(text='Комплект документов', callback_data='ssol_process-docs')
ssol_process_shedule = InlineKeyboardButton(text='Режим работы кассы и ПОС', callback_data='ssol_process-shedule')
ssol_process_transfer = InlineKeyboardButton(text='Трансфер', callback_data='ssol_process-transfer')
ssol_process_bilet = InlineKeyboardButton(text='Профсоюзный билет', callback_data='ssol_process-bilet')
ssol_process_docs_take = InlineKeyboardButton(text='Получить заявление', callback_data='ssol_process-docs-take')


# markups
ssol_process_markup = InlineKeyboardMarkup(row_width=1).add(ssol_process_docs, ssol_process_transfer,
                                                            ssol_process_bilet, ssol_process_shedule,
                                                            return_to_ssol_main)

ssol_process_docs_markup = InlineKeyboardMarkup(row_width=1).add(ssol_process_docs_take, return_to_ssol_process)
ssol_return_to_process = InlineKeyboardMarkup().add(return_to_ssol_process)
ssol_return_to_types_markup = InlineKeyboardMarkup().add(return_to_ssol_types)
ssol_return_to_main = InlineKeyboardMarkup().add(return_to_ssol_main)

# ----------END SSOL ZARYA----------

# ----------Contacts----------

contacts_markup = InlineKeyboardMarkup(row_width=1).add(insta_url, vk_url)
