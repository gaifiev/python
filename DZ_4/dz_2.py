# 2.Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
array = int(input("Введите число: "))
i = 2
array1 = []
n = array
while i <= array:
    if array % i == 0:
        array1.append(i)
        array //= i
        i = 2
    else:
        i += 1
print(array1)
