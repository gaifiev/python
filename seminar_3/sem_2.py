# 2 Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке
# строк некое число.
def SearchList(arr, number):
    if str(number) in arr:
        return 'yes'
    return 'no'


list_1 = ['hello', '12', 'red', '567']
print(SearchList(list_1, 3243546576))
