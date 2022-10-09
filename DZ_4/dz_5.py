# 5 Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

with open('DZ_4\mnogochlen_stepeni_k.txt', 'r') as file:
    mnogochlen1 = file.read()
    mnogochlen1 = mnogochlen1[0:-4]

with open('DZ_4\mnogochlentwo.txt', 'r') as file:
    mnogochlen2 = file.read()

with open('DZ_4\sum_mnogoclenov.txt', 'w', encoding='utf-8') as file:
    file.write(f'{mnogochlen1} + {mnogochlen2}')
