import keyboards as kb
import info

API_TOKEN = 'API_TOKEN'


dict_mm = {'Общежития': [info.dorm_main_info, kb.dorm_keyb_m_up],
           'Стипендии': [info.scholarship_main_info, kb.scholarship_markup],
           'Проекты': [info.proj_main_menu_info, kb.projects_main_menu_markup],
           'Заря': [info.ssol_main_info, kb.ssol_main_markup],
           'РЖД - бонус': [info.rzd_bonus_main_info, kb.rzd_markup],
           'О профсоюзе': [info.about_pos, kb.about_pos_markup],
           'Контакты': [info.contacts_main_info, kb.contacts_markup]}

dict_dorm = {'undergrad': [info.dorm_undergrad, kb.dorm_undergrad_keyb_m_up],
             'underdocs': ['Выберите нужную категорию', kb.dorm_underdocs_keyb_m_up],
             'summer': [info.dorm_summer, kb.dorm_summer_markup],
             'summer-do': [info.dorm_summer_do, kb.dorm_summer_do_markup],
             'already-living': [info.dorm_underdocs_already_living, kb.dorm_return_to_underdocs_markup],
             'do-not-live': [info.dorm_underdocs_do_not_live, kb.dorm_return_to_underdocs_markup],
             'master': [info.dorm_underdocs_master, kb.dorm_return_to_underdocs_markup],
             'enrollee': [info.dorm_enrollee, kb.dorm_enrolee_markup],
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
                    'pgss': [info.scholarship_pgss, kb.pgss_markup]}

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
             'process-shedule': [info.ssol_process_shedule, kb.ssol_return_to_process],
             'quiz': [info.ssol_quiz, kb.ssol_return_to_main]}

dict_returns = {'dorm-main': [info.dorm_main_info, kb.dorm_keyb_m_up],
                'dorm-list': [info.dorm_list, kb.dorm_list_markup],
                'dorm-summer': [info.dorm_summer, kb.dorm_summer_markup],
                'undergrad': [info.dorm_undergrad, kb.dorm_undergrad_keyb_m_up],
                'underdocs': ['Выберите нужную категорию', kb.dorm_underdocs_keyb_m_up],
                'scholarship': [info.scholarship_main_info, kb.scholarship_markup],
                'gss': [info.scholarship_pgas, kb.gss_markup],
                'gas': [info.scholarship_gas, kb.gas_markup],
                'rzd': [info.rzd_bonus_main_info, kb.rzd_markup],
                'ssol': [info.ssol_main_info, kb.ssol_main_markup],
                'types': [info.ssol_types, kb.ssol_types_markup],
                'process': [info.ssol_process, kb.ssol_process_markup],
                'proj': [info.proj_main_menu_info, kb.projects_main_menu_markup]}


bad_words = ['хуй', 'пизда']
