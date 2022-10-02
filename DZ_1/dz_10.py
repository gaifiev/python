# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
import math

a1 = float(input("Координат A1: "))
b1 = float(input("Координат B1: "))
a2 = float(input("Координат A2: "))
b2 = float(input("Координат B2: "))
print(
    f"Расстояние между ними в 2D пространстве = {math.sqrt( ((b2 - b1) ** 2) + ((a2 - a1) ** 2))}")