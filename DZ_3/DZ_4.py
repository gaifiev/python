# 4.Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

arr = int(input("Введите число для преобразования десятичное число в двоичное: "))
b = bin(arr)  # встроенная функция преобразования
print(b)
