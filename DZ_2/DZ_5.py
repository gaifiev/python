# Реализуйте алгоритм перемешивания списка.
import random


def paddling(initial_list):
    list = initial_list[:]
    list_length = len(list)
    for i in range(list_length):
        gen = random.randint(0, list_length - 1)
        temp = list[i]
        list[i] = list[gen]
        list[gen] = temp
    return list


list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
paddling_list = paddling(list)
print("Изначальный список: ")
print(list)
print("Перемешанный список: ")
print(paddling_list)
