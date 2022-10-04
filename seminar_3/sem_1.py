# 1 Реализуйте алгоритм задания случайных чисел без использования встроенного генератора
# псевдослучайных чисел.
import time

print(str(time.time_ns())[-4] + str(time.time_ns())[-3])

print(int(str(time.time_ns())[-5] +
      str(time.time_ns())[-4] + str(time.time_ns())[-3]))
