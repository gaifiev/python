# 3 Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее
# кратное) этих двух чисел.
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
s = a * b
while a != b:
    if a > b:
        a -= b
    else:
        b -= a
print(s // a)