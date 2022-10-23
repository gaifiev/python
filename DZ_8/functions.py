def Menu() -> int:
    print("\n" + "=" * 20)
    print("Компания 'Газпром'\nВыберите необходимое действие:")
    print("1. Найти сотрудника")
    print("2. Сделать выборку сотрудников по должности")
    print("3. Сделать выборку сотрудников по з/п")
    print("4. Добавить сотрудника")
    print("5. Удалить сотрудника")
    print("6. Закончить работу")
    return int(input("Введите номер необходимого действия: "))


def Last_name():
    name = input('Введите фамилию работника: ')
    return name


def Post():
    job = input('Введите должность работника: ')
    return job


def Pay():
    money = input('Введите сумму з/п: ')
    return money


def AddPersonal():
    personal = input(
        'Введите данные сотрудника в формате: id, фамилия, имя, профессия, з/п (р.) Например, Иванов Иван Программист 200000 р.: ')
    return personal


def Delete():
    with open('Data_base.csv', 'r', encoding='utf-8') as data:
        print(data.read())
        delpers = int(input('Введите номер сотрудника для удаления: '))
        return delpers
