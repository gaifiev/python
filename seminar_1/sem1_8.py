# Сообщить в какой четверти координатной плоскости или на какойоси находится точка с координатами Х и У.

try:
    x = float(input("Введите значение координаты x: "))
    y = float(input("Введите значение координаты y: "))
except:
    print("Вы ввели не число!!! Попробуйте снова")
else:
    if x == 0 and y == 0:
        print("Точка в центре оси координат")
    elif x == 0:
        if y > 0:
            print("Точка лежит на оси y между 1 и 2 четвертями")
        else:
            print("Точка лежит на оси y между 3 и 4 четвертями")
    elif y == 0:
        if x > 0:
            print("Точка лежит на оси x между 1 и 4 четвертями")
        else:
            print("Точка лежит на оси x между 2 и 3 четвертями")
    elif x > 0:
        if y > 0:
            print("Точка находится в 1 четверти")
        else:
            print("Точка находится в 4 четверти")
    else:
        if y > 0:
            print("Точка находится в 2 четверти")
        else:
            print("Точка находится в 3 четверти")
