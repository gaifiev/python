# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# print(''.join(input().lower().split('абв')))  # удаляет содержание абв из слов

# print(' '.join([i for i in input().lower().split() if 'абв' not in i]))

stroka = input().split()
arr = [i for i in stroka if 'абв' not in i.lower()]
new_str = ' '.join(arr)
print(new_str)
