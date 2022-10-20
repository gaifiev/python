def log(info):
    with open('log.txt', 'a', encoding='utf-8') as f:
        if len(info.split()) == 1:
            f.write(f'Экспорт - {info}' + '\n')
        else:
            f.write(f'Импорт - {info}' + '\n')
