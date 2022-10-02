# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
from functools import reduce

n = int(input("Введите число n: "))
list = []
a = 0
for n in range(1, n + 1):
    num = (1 + 1 / n) ** n
    list.append(num)
    a += num
print(f"Список из {n} чисел: ")
print(list)
print(f"Cумма чисел  {a}")
