# 7 Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# 1 solution
# x = (input('Введите первое число: '))
# y = (input('Введите второе число: '))
# z = (input('Введите третье число: '))

# if not (x or y or z) == (not (x)) and not (y) and not (z):
#     print('Утверждение верно')
# else:
#     print('Утверждение ложно')

# 2 solution
def logical_statement(x, y, z):
    print(f"¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} is {(not (x or y or z)) == (not x and not y and not z)}")
    return (not (x or y or z)) == (not x and not y and not z)


if (logical_statement(0, 0, 0) and logical_statement(0, 0, 1) and logical_statement(0, 1, 0) and
    logical_statement(0, 1, 1) and logical_statement(1, 0, 0) and logical_statement(1, 0, 1) and
        logical_statement(1, 1, 0) and logical_statement(1, 1, 1)):
    print("Истинно")
else:
    print("Ложно")
