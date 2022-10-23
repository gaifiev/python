# def log(info):
#     with open('log.txt', 'a', encoding='utf-8') as f:
#         if len(info.split()) == 1:
#             f.write(f'Экспорт - {info}' + '\n')
#         else:
#             f.write(f'Импорт - {info}' + '\n')


def log1(info1):
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(f'Удаление - {info1}' + '\n')


def log2(info2):
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(f'Добавление сотрудника - {info2}' + '\n')


def log3(info2):
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(f'Поиск сотрудника - {info2}' + '\n')


def log4(info2):
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(f'Выборка сотрудников по должности - {info2}' + '\n')


def log5(info2):
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(f'Выборка сотрудников по з/п - {info2}' + '\n')
