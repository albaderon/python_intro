import math
import random

def print_delim(num_repits=80):
    print('='*num_repits)


def pretty_print(value):
    print('Result =', value)
    print_delim()


def pretty_task(value):
    print_delim()
    print("Task number", value)

# =====================================================================================================
# Task 9.Нормировать одномерный массив случайных чисел. Нормирование означает приведение всех значений
# массива к интервалу [-1;1], причем максимальное абсолютное значение элементов после нормирование
# должно быть равно 1. Например, последовательность {-5, 3, 4} после нормирование будет
# выглядеть {-1, 0.6, 0.8}
# =====================================================================================================

pretty_task(9)

str = [random.randint(-5,5) for x in range(3)]
print(str)
max_elem = max(str)
min_elem = min(str)
if abs(min_elem) <= max_elem:
    max_abs = max_elem
else:
    max_abs = abs(min_elem)

for i, elem  in enumerate(str):
    str[i] /= max_abs
print(str)





