def Money(number):
    with open('Data_base.csv', 'r', encoding='utf-8') as data:
        info = data.read().splitlines()
        for salary in info:
            if number in salary:
                salary = salary.split(' ')
                if number in salary:
                    print(*salary)