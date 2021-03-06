import keyboards as kb
import info

API_TOKEN = 'TOKEN'

dict_mm = {'Общежития 🏡': [info.dorm_main_info, kb.dorm_keyb_m_up],
           'Стипендии 💰': [info.scholarship_main_info, kb.scholarship_markup],
           'Проекты 🔥': [info.proj_main_menu_info, kb.projects_main_menu_markup],
           'Заря 🌳': [info.ssol_main_info, kb.ssol_main_markup],
           'РЖД - бонус 🎁': [info.rzd_bonus_main_info, kb.rzd_markup],
           'О профсоюзе 🏠': [info.about_pos, kb.about_pos_markup],
           'Контакты ☎': [info.contacts_main_info, kb.contacts_markup]}

dict_dorm = {'undergrad': [info.dorm_undergrad, kb.dorm_undergrad_keyb_m_up],
             'underdocs': ['Выберите нужную категорию', kb.dorm_underdocs_keyb_m_up],
             'summer': [info.dorm_summer, kb.dorm_summer_markup],
             'summer-do': [info.dorm_summer_do, kb.dorm_summer_do_markup],
             'already-living': [info.dorm_underdocs_already_living, kb.dorm_return_to_underdocs_markup],
             'do-not-live': [info.dorm_underdocs_do_not_live, kb.dorm_return_to_underdocs_markup],
             'master': [info.dorm_underdocs_master, kb.dorm_return_to_underdocs_markup],
             'enrollee': [info.dorm_enrollee, kb.dorm_enrolee_markup],
             'enrolle-docs': [info.enrolle_docs, kb.dorm_enrolle_docs_markup],
             'list': [info.dorm_list, kb.dorm_list_markup],
             '2': [info.dorm_2, kb.dorm_2_markup],
             '4': [info.dorm_4, kb.dorm_4_markup],
             '6': [info.dorm_6, kb.dorm_6_markup],
             '7': [info.dorm_7, kb.dorm_7_markup],
             '8': [info.dorm_8, kb.dorm_8_markup],
             '9': [info.dorm_9, kb.dorm_9_markup]}

dict_scholarship = {'gas': [info.scholarship_gas, kb.gas_markup],
                    'gas-size': [info.scholarship_gas_size, kb.return_to_gas_markup],
                    'gas-criteries': [info.scholarship_gas_criteries, kb.return_to_gas_markup],
                    'pgas': [info.scholarship_pgas, kb.pgas_markup],
                    'gss': [info.scholarship_gss, kb.gss_markup],
                    'gss-size': [info.scholarship_gss_size, kb.return_to_gss_markup],
                    'gss-people': [info.scholarship_gss_people, kb.return_to_gss_markup],
                    'gss-where': [info.scholarship_gss_where, kb.return_to_gss_markup],
                    'gss-docs': [info.scholarship_gss_docs, kb.return_to_gss_markup],
                    'pgss': [info.scholarship_pgss, kb.pgss_markup],
                    'pgss-people': [info.pgss_people, kb.return_to_pgss_markup],
                    'pgss-size': [info.pgss_size, kb.return_to_pgss_markup],
                    'name': [info.name_main, kb.name_markup],
                    'name-city': [info.name_city, kb.name_city_markup],
                    'name-city-size': [info.name_city_size, kb.return_to_name_city_markup],
                    'name-city-people': [info.name_city_people, kb.return_to_name_city_markup],
                    'name-city-where': [info.name_city_where, kb.return_to_name_city_markup],
                    'name-city-docs': [info.name_city_docs, kb.return_to_name_city_markup],
                    'name-potanin': [info.name_potanin, kb.return_to_scholarship_name_markup],
                    'alpha': [info.alpha_main, kb.alpha_markup]}

dict_rzd = {'participant': [info.rzd_participant, kb.rzd_return_to_main_menu_markup],
            'timing': [info.rzd_timing, kb.rzd_return_to_main_menu_markup]}

dict_projects = {'dnk': [info.proj_dnk, kb.proj_dnk_markup],
                 'jz': [info.proj_jz, kb.proj_jz_markup],
                 'rv': [info.proj_rv, kb.proj_rv_markup],
                 'cgk': [info.proj_cgk, kb.proj_cgk_markup],
                 'bdj': [info.proj_bdj, kb.proj_bdj_markup],
                 'sd': [info.proj_sd, kb.proj_sd_markup],
                 'kongress': [info.proj_kongress, kb.proj_kongress_markup],
                 'sso': [info.proj_sso, kb.proj_sso_markup]}

dict_ssol = {'types': [info.ssol_types, kb.ssol_types_markup],
             'health': [info.ssol_health, kb.ssol_return_to_types_markup],
             'battle': [info.ssol_battle, kb.ssol_return_to_types_markup],
             'choice': [info.ssol_choice, kb.ssol_return_to_types_markup],
             'creative': [info.ssol_creative, kb.ssol_return_to_types_markup],
             'cost': [info.ssol_cost, kb.ssol_return_to_main],
             'process': [info.ssol_process, kb.ssol_process_markup],
             'process-docs': [info.ssol_process_docs, kb.ssol_process_docs_markup],
             'process-transfer': [info.ssol_process_transfer, kb.ssol_return_to_process],
             'process-bilet': [info.ssol_process_bilet, kb.ssol_return_to_process],
             'process-shedule': [info.ssol_process_shedule, kb.ssol_return_to_process]}

dict_contacts = {'nngu': [info.contacts_nngu, kb.contacts_nngu_markup],
                 'dekanat': [info.contacts_dekanat, kb.contacts_dekanat_markup],
                 'mfc': [info.contacts_mfc, kb.return_to_contacts_nngu_markup],
                 'otdel': [info.contacts_otdel, kb.return_to_contacts_nngu_markup],
                 'dekanat-iitmm': [info.dek_iitmm, kb.return_to_contacts_dekanat_markup],
                 'dekanat-imomi': [info.dek_imomi, kb.return_to_contacts_dekanat_markup],
                 'dekanat-ibbm': [info.dek_ibbm, kb.return_to_contacts_dekanat_markup],
                 'dekanat-ifizj': [info.dek_ifizj, kb.return_to_contacts_dekanat_markup],
                 'dekanat-iep': [info.dek_iep, kb.return_to_contacts_dekanat_markup],
                 'dekanat-fsn': [info.dek_fsn, kb.return_to_contacts_dekanat_markup],
                 'dekanat-uf': [info.dek_uf, kb.return_to_contacts_dekanat_markup],
                 'dekanat-rf': [info.dek_rf, kb.return_to_contacts_dekanat_markup],
                 'dekanat-hf': [info.dek_hf, kb.return_to_contacts_dekanat_markup],
                 'dekanat-vshopf': [info.dek_vshopf, kb.return_to_contacts_dekanat_markup],
                 'dekanat-fks': [info.dek_fks, kb.return_to_contacts_dekanat_markup],
                 'dekanat-fzf': [info.dek_fzf, kb.return_to_contacts_dekanat_markup]}

dict_returns = {'dorm-main': [info.dorm_main_info, kb.dorm_keyb_m_up],
                'dorm-list': [info.dorm_list, kb.dorm_list_markup],
                'dorm-summer': [info.dorm_summer, kb.dorm_summer_markup],
                'undergrad': [info.dorm_undergrad, kb.dorm_undergrad_keyb_m_up],
                'underdocs': ['Выберите нужную категорию', kb.dorm_underdocs_keyb_m_up],
                'scholarship': [info.scholarship_main_info, kb.scholarship_markup],
                'gss': [info.scholarship_pgas, kb.gss_markup],
                'gas': [info.scholarship_gas, kb.gas_markup],
                'pgss': [info.scholarship_pgss, kb.pgss_markup],
                'scholarship-name': [info.name_main, kb.name_markup],
                'scholarship-name-city': [info.name_city, kb.name_city_markup],
                'rzd': [info.rzd_bonus_main_info, kb.rzd_markup],
                'ssol': [info.ssol_main_info, kb.ssol_main_markup],
                'types': [info.ssol_types, kb.ssol_types_markup],
                'process': [info.ssol_process, kb.ssol_process_markup],
                'proj': [info.proj_main_menu_info, kb.projects_main_menu_markup],
                'contacts': [info.contacts_main_info, kb.contacts_markup],
                'nngu': [info.contacts_nngu, kb.contacts_nngu_markup],
                'dekanat': [info.contacts_dekanat, kb.contacts_dekanat_markup],
                'dorm-enrolle': [info.dorm_enrollee, kb.dorm_enrolee_markup],
                'admin-main': ['Меню администратора, выбирай, что тебе нужно сделать', kb.admin_main_markup]}

buttons_names = {'dorm_4': 'Общежития/Список Общежитий/Общежитие 4',
                 'dorm_6': 'Общежития/Список Общежитий/Общежитие 6',
                 'dorm_7': 'Общежития/Список Общежитий/Общежитие 7',
                 'dorm_8': 'Общежития/Список Общежитий/Общежитие 8',
                 'dorm_9': 'Общежития/Список Общежитий/Общежитие 9',
                 'scholarship_gas': 'Стипендии/ГАС',
                 'scholarship_gss': 'Стипендии/ГСС',
                 'scholarship_pgas': 'Стипендии/ПГАС',
                 'scholarship_pgss': 'Стипендии/ПГСС',
                 'dorm_summer-docs': 'Общежития/Старшекурсники Лето/Получить Документы',
                 'proj_dnk': 'Проекты/ДНК',
                 'ssol_types': 'Заря/Смены',
                 'proj_jz': 'Проекты/Живая Земля',
                 'contacts_dekanat-rf': 'Контакты/Контакты ННГУ/Декатаны/РФ',
                 'proj_rv': 'Проекты/Разумный Выбор',
                 'scholarship_pgss-size': 'Стипендии/ПГСС/Размер ПГСС',
                 'scholarship_gss-size': 'Стипендии/ГСС/Размер стипендии',
                 'scholarship_gss-people': 'Стипендии/ГСС/Кому положена социальная стипенди?',
                 'scholarship_gss-where': 'Стипендии/ГСС/Куда подавать',
                 'scholarship_gss-docs': 'Стипендии/ГСС/Какие документы нужны',
                 'proj_sd': 'Проекты/Сильные духом',
                 'proj_cgk': 'Проекты/Что? Где? Когда?',
                 'scholarship_gas-size': 'Стипендии/ГАС/Размер стипендии',
                 'scholarship_gas-criteries': 'Стипендии/ГАС/Критерии получения',
                 'proj_kongress': 'Проекты/Конгресс',
                 'proj_bdj': 'Проекты/Брусничный Джем',
                 'contacts_dekanat': 'Контакты/Контакты ННГУ/Деканаты',
                 'contacts_dekanat-fzf': 'Контакты/Контакты ННГУ/Декатаны/ФЗФ',
                 'ssol_cost': 'Заря/Стоимость',
                 'ssol_process': 'Заря/Процесс приобретения путевок',
                 'proj_sso': 'Проекты/Конкурс ССО',
                 'welcome_message': 'Привет! 👋',
                 'rzd_participant': 'РЖД - бонус/Как стать участником программы',
                 'rzd_timing': 'РЖД - бонус/Сроки действия программы',
                 'Стипендии': 'Стипендии',
                 'Контакты': 'Контакты',
                 'О профсоюзе': 'О профсоюзе',
                 'Медиа ПОС': 'Медиа ПОС',
                 'contacts_nngu': 'Контакты/Контакты ННГУ',
                 'dorm_underdocs': 'Общежития/Старшекурсники/Комплект Документов',
                 'dorm_already-living': 'Общежития/Старшекурсники/Комплект Документов/Уже живу',
                 'dorm_do-not-live': 'Общежития/Старшекурсники/Комплект Документов/Не живу',
                 'dorm_master': 'Общежития/Старшекурсники/Комплект Документов/Магистр',
                 'dorm_enrollee': 'Общежития/Абитуриенты',
                 'dorm_summer': 'Общежития/Старшекурсники Лето',
                 'dorm_summer-do': 'Общежития/Старшекурсники Лето/Что мне надо сделать?',
                 'dorm_list': 'Общежития/Список Общежитий',
                 'dorm_2': 'Общежития/Список Общежитий/Общежитие 2',
                 'Заря': 'Заря',
                 'return_to_mm': 'Вернуться в главное меню',
                 'РЖД - бонус': 'РЖД - бонус',
                 'Проекты': 'Проекты',
                 'Общежития': 'Общежития',
                 'dorm_undergrad': 'Общежития/Старшекурсники',
                 'contacts_dekanat-uf': 'Контакты/Контакты ННГУ/Деканаты/ЮФ',
                 'contacts_dekanat-hf': 'Контакты/Контакты ННГУ/Деканаты/ХФ',
                 'contacts_dekanat-vshopf': 'Контакты/Контакты ННГУ/Деканаты/ВШОПФ',
                 'contacts_dekanat-fks': 'Контакты/Контакты ННГУ/Деканаты/ФКС',
                 'contacts_dekanat-iitmm': 'Контакты/Контакты ННГУ/Деканаты/ИИТММ',
                 'contacts_dekanat-imomi': 'Контакты/Контакты ННГУ/Деканаты/ИМОМИ',
                 'contacts_dekanat-ibbm': 'Контакты/Контакты ННГУ/Деканаты/ИББМ',
                 'contacts_dekanat-ifizj': 'Контакты/Контакты ННГУ/Деканаты/ИФИЖ',
                 'contacts_dekanat-fsn': 'Контакты/Контакты ННГУ/Деканаты/ФСН',
                 'contacts_dekanat-iep': 'Контакты/Контакты ННГУ/Деканаты/ИЭП',
                 'ssol_process-docs-take': 'Заря/Процедура приобретения путевки/Комплект документов/Получить заявление',
                 'ssol_process-transfer': 'Заря/Процедура приобретения путевки/Трансфер',
                 'ssol_process-bilet': 'Заря/Процедура приобретения путевки/Профсоюзный билет',
                 'ssol_process-shedule': 'Заря/Процедура приобретения путевки/Режим работы кассы и ПОС',
                 'ssol_quiz': 'Заря/Розыгрыш путевки',
                 'contacts_mfc': 'Контакты/Контакты ННГУ/МФЦ',
                 'contacts_otdel': 'Контакты/Контакты ННГУ/Стипендиальный отдел',
                 'scholarship_pgss-people': 'Стипендии/ПГСС/Кому положена ПГСС',
                 'ssol_health': 'Заря/Смены/Отдыхай на здоровье',
                 'ssol_battle': 'Заря/Смены/Битва студсоветов',
                 'ssol_choice': 'Заря/Смены/Разумный Выбор',
                 'ssol_creative': 'Заря/Смены/Креативные индустрии',
                 'ssol_process-docs': 'Заря/Процедура приобретения путевки/Комплект документов',
                 'scholarship_name': 'Стипендии/Именные стипендии',
                 'dorm_enrolle-docs': 'Общежития/Абитуриенты/Перечень документов',
                 'scholarship_name-city': 'Стипендии/Именные стипендии/Главы города',
                 'scholarship_alpha': 'Стипендии/Альфа шанс',
                 'scholarship_name-city-docs': 'Стипендии/Именные стипендии/Главы города/Комплект Документов',
                 'scholarship_name-city-people': 'Стипендии/Именные стипендии/Главы города/Кому положена?',
                 'scholarship_name-potanin': 'Стипендии/Именные стипендии/Потанина',
                 'dorm_enrolle-docs-take': 'Общежития/Абитуриенты/Перечень документов/Получить документы',
                 'scholarship_name-city-size': 'Стипендии/Именные стипендии/Главы города/Размер стипендии',
                 'scholarship_name-city-where': 'Стипендии/Именные стипендии/Главы города/Куда подавать?'}
