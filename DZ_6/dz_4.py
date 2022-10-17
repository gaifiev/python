# 2.Задача 1 из домашней работы 3. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# map

array = list(map(int, input("Введите числа через пробел: ").split()))
otbor = str([array[item] for item in range(1, len(array), 2)]).strip('[]')
sum_array = sum(array[item] for item in range(1, len(array), 2))

print(
    f'Cумма чисел на нечётных позициях: {otbor} равна {sum_array}.')
