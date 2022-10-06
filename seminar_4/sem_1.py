# 1 Задайте строку из набора чисел. Напишите программу, которая покажет большее и
# меньшее число. В качестве символа-разделителя используйте пробел.
stroka = '123 145 184 1900'
list_1 = stroka.split()
max = int(list_1[0])
min = int(list_1[0])
for i in list_1:
    if int(i) > max:
        max = int(i)
    if int(i) < min:
        min = int(i)
print(max)
print(min)
