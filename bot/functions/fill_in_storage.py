"""Ручное заполнение таблиц"""

from storage import MongodbService
from pprint import pprint
import click

storage = MongodbService()


@click.group()
def cli():
    pass


@click.command()
def save_test_data():
    schedule = {'group': 'ИБб-18-1',
                'schedule': [{'day': 'понедельник',
                              'lessons': [{'aud': '',
                                           'info': '( Практ.,  )',
                                           'name': 'Элективные курсы по физической культуре и спорту',
                                           'prep': '',
                                           'time': '8:15',
                                           'week': 'even'},
                                          {'aud': 'Ж309',
                                           'info': '( Практ.,  )',
                                           'name': 'Документоведение',
                                           'prep': 'Иванов Н.А.',
                                           'time': '8:15',
                                           'week': 'odd'},
                                          {'aud': 'ДАМФа',
                                           'info': '( Практ.,  )',
                                           'name': 'Цифровая обработка сигналов',
                                           'prep': 'Дмитриев А. А.',
                                           'time': '10:00',
                                           'week': 'even'},
                                          {'aud': 'Ж317',
                                           'info': '( Практ.,  )',
                                           'name': 'Теория информации',
                                           'prep': 'Афанасьева Ж.С.',
                                           'time': '10:00',
                                           'week': 'odd'},
                                          {'aud': 'И305',
                                           'info': '( Лекция,  )',
                                           'name': 'Математическая логика и теория алгоритмов',
                                           'prep': 'Богданов А.И.',
                                           'time': '11:45',
                                           'week': 'all'},
                                          {'aud': 'Ж309',
                                           'info': '( Практ.,  )',
                                           'name': 'Теория принятия решений',
                                           'prep': 'Маринов А.А.',
                                           'time': '13:45',
                                           'week': 'all'},
                                          {'aud': 'онлайн',
                                           'info': '( Лекция,  )',
                                           'name': 'Теория информации',
                                           'prep': 'Афанасьев А.Д.',
                                           'time': '17:10',
                                           'week': 'even'},
                                          {'aud': 'онлайн',
                                           'info': '( Лекция,  )',
                                           'name': 'Теория информации',
                                           'prep': 'Афанасьев А.Д.',
                                           'time': '17:10',
                                           'week': 'odd'},
                                          {'aud': 'онлайн',
                                           'info': '( Практ., подгруппа 1 )',
                                           'name': 'Иностранный язык в сфере профессиональной коммуникации',
                                           'prep': '',
                                           'time': '18:45',
                                           'week': 'all'},
                                          {'aud': 'онлайн',
                                           'info': '( Практ., подгруппа 2 )',
                                           'name': 'Иностранный язык в сфере профессиональной коммуникации',
                                           'prep': '',
                                           'time': '18:45',
                                           'week': 'all'}]},
                             {'day': 'среда',
                              'lessons': [{'aud': 'Ж313',
                                           'info': '( Лаб. раб., подгруппа 1 )',
                                           'name': 'Математические основы криптологии',
                                           'prep': 'Тюрнев А.С.',
                                           'time': '8:15',
                                           'week': 'all'},
                                          {'aud': 'ДАМФа',
                                           'info': '( Лаб. раб., подгруппа 2 )',
                                           'name': 'Цифровая обработка сигналов',
                                           'prep': 'Дмитриев А. А.',
                                           'time': '8:15',
                                           'week': 'all'},
                                          {'aud': 'ДАМФа',
                                           'info': '( Лаб. раб., подгруппа 1 )',
                                           'name': 'Цифровая обработка сигналов',
                                           'prep': 'Дмитриев А. А.',
                                           'time': '10:00',
                                           'week': 'all'},
                                          {'aud': 'Ж313',
                                           'info': '( Лаб. раб., подгруппа 2 )',
                                           'name': 'Математические основы криптологии',
                                           'prep': 'Тюрнев А.С.',
                                           'time': '10:00',
                                           'week': 'all'},
                                          {'aud': '',
                                           'info': '( Практ.,  )',
                                           'name': 'Элективные курсы по физической культуре и спорту',
                                           'prep': '',
                                           'time': '11:45',
                                           'week': 'even'},
                                          {'aud': '',
                                           'info': '( Практ.,  )',
                                           'name': 'Элективные курсы по физической культуре и спорту',
                                           'prep': '',
                                           'time': '11:45',
                                           'week': 'odd'},
                                          {'aud': 'И305',
                                           'info': '( Лекция,  )',
                                           'name': 'Теория принятия решений',
                                           'prep': 'Маринов А.А.',
                                           'time': '23:45',
                                           'week': 'all'}]},
                             {'day': 'четверг',
                              'lessons': [{'aud': 'И305',
                                           'info': '( Лекция,  )',
                                           'name': 'Документоведение',
                                           'prep': 'Иванов Н.А.',
                                           'time': '8:15',
                                           'week': 'even'},
                                          {'aud': 'Дамф.',
                                           'info': '( Лекция,  )',
                                           'name': 'Цифровая обработка сигналов',
                                           'prep': 'Дмитриев А. А.',
                                           'time': '8:15',
                                           'week': 'odd'},
                                          {'aud': 'И305',
                                           'info': '( Практ.,  )',
                                           'name': 'Математическая логика и теория алгоритмов',
                                           'prep': 'Богданов А.И.',
                                           'time': '10:00',
                                           'week': 'all'},
                                          {'aud': 'Ж317',
                                           'info': '( Лекция,  )',
                                           'name': 'Математические основы криптологии',
                                           'prep': 'Тюрнев А.С.',
                                           'time': '11:45',
                                           'week': 'all'},
                                          {'aud': 'Ж309',
                                           'info': '( Практ.,  )',
                                           'name': 'Математические основы криптологии',
                                           'prep': 'Тюрнев А.С.',
                                           'time': '13:45',
                                           'week': 'all'}]},
                             {'day': 'пятница, 18 сентября ',
                              'lessons': [{'aud': 'К313',
                                           'info': '( Практ.,  )',
                                           'name': 'Документоведение',
                                           'prep': 'Иванов Н.А.',
                                           'time': '8:15',
                                           'week': 'even'},
                                          {'name': 'свободно', 'time': '8:15', 'week': 'odd'},
                                          {'aud': 'К305',
                                           'info': '( Лекция,  )',
                                           'name': 'Защита персональных данных (факультатив)',
                                           'prep': 'Иванов Н.А.',
                                           'time': '10:00',
                                           'week': 'even'},
                                          {'name': 'свободно', 'time': '10:00', 'week': 'odd'},
                                          {'aud': 'Ж317',
                                           'info': '( Практ.,  )',
                                           'name': 'Защита персональных данных (факультатив)',
                                           'prep': 'Иванов Н.А.',
                                           'time': '11:45',
                                           'week': 'even'},
                                          {'name': 'свободно', 'time': '11:45', 'week': 'odd'}]}]
                }
    storage.save_data(collection='schedule', data=schedule)


@click.command()
def save_full_data():
    storage.save_institutes(
        [{'name': 'Аспирантура'}, {'name': 'Байкальский институт БРИКС'}, {'name': 'ИАиТ'}, {'name': 'ИАСиД'},
         {'name': 'ИВТ'}, {'name': 'Институт заочно-вечернего обучения'}, {'name': 'ИИТиАД'}, {'name': 'ИН'},
         {'name': 'ИЭУиП'}, {'name': 'ИЭ'}])

    storage.save_courses([
        {'name': '1 курс', 'institute': 'ИВТ'},
        {'name': '2 курс', 'institute': 'ИВТ'},
        {'name': '3 курс', 'institute': 'ИВТ'},
        {'name': '4 курс', 'institute': 'ИВТ'},

        {'name': '1 курс', 'institute': 'ИИТиАД'},
        {'name': '2 курс', 'institute': 'ИИТиАД'},
        {'name': '3 курс', 'institute': 'ИИТиАД'},
        {'name': '4 курс', 'institute': 'ИИТиАД'},
        {'name': '5 курс', 'institute': 'ИИТиАД'},
    ])

    storage.save_groups([
        {
            'name': 'ИБб-18-1',
            'institute': 'ИИТиАД',
            'course': '3 курс'
        },
        {
            'name': 'ИБб-18-2',
            'institute': 'ИИТиАД',
            'course': '3 курс'
        },
        {
            'name': 'ИБб-20-1',
            'institute': 'ИИТиАД',
            'course': '1 курс'
        }
    ])


cli.add_command(save_test_data)
cli.add_command(save_full_data)

if __name__ == '__main__':
    cli()
