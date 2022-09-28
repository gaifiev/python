# 4 Показать первую цифру дробной части числа.
# num = float(input("Введите дробное число: "))
# round_num = int(num)
# result = (num - round_num) * 10
# print(f'Первая цифра дробной части: {int(result)}')

def first_float():
    n = input("Введите вещественное число: ")
    n_list = n.split('.')
    print(n_list)
    print(n_list[1][0])


first_float()
