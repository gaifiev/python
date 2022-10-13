# 1 В файле находится N натуральных чисел, записанных через пробел. Среди чисел не
# хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.


# with open('1.txt', 'r', encoding='utf-8') as file:
#     print(file.readlines())

with open('1.txt', 'r', encoding='utf-8') as file:
    arr = file.readlines()
    arr = [int(i) for i in arr[0].split()]
    print(arr)
