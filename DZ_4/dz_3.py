# 3.Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
array = [1, 2, 7, 2, 4, 4, 7, 6, 3]
array = list(set(array))
# Set — это неупорядоченная коллекция уникальных элементов(отсутствующих повторяющиеся значения)
print(array)