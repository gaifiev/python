# Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементовна указанных позициях.
# Позиции хранятся в списке file.txt - создайте этот список
# (например: positions = [1, 3, 6]).
from random import randint

with open('file.txt', 'w') as data:
    data.write('2\n')
    data.write('2\n')
    data.write('4\n')
    data.write('8\n')
    data.write('8\n')


def get_numbers(n):
    return [i for i in range(-n, n + 1)]
    # return [randint(-n/2, n) for i in range(-n, n + 1)]


def get_data_from_file(path):
    data = open(path, 'r')
    dlist = [int(line.strip()) for line in data]
    data.close()
    return dlist


def get_mult(numbers, datalist):
    mult = 1
    for i in datalist:
        mult *= numbers[i]
    return mult


path = 'file.txt'
n = 10
datalist = get_data_from_file(path)
numbers = get_numbers(n)

print('Заданный список элементов: ', numbers)
print('Отображение позиций нужных элементов из файла', datalist,)
print(get_mult(numbers, datalist))
