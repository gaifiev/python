# 5. Реализуйте алгоритм перемешивания списка.
from random import Random, randint

N = int(input('Введите число '))
numbers = [randint(-N, N+1) for i in range(N)]
print("Изначальный список: ")
print(numbers)


def smeshiv(numbers):
    list = numbers[:]
    numbers_length = len(list)
    for i in range(numbers_length):
        index = randint(0, numbers_length - 1)
        temp = list[i]
        list[i] = list[index]
        list[index] = temp
    return list


print("Перемешанный список: ")
print(smeshiv(numbers))
