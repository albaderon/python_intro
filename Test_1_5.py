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


# ============================================================================================
# Task 5.Создать программу, выводящую на экран ближайшее к 10 из двух чисел,
# введенных пользователем. Например, среди чисел 8,5 и 11,45 ближайшее к десяти 11,45.
# ============================================================================================

pretty_task(5)

def is_short_number(x,y):
    compare_number = 10

    if abs(10-x) < abs(10-y):
        result = x
    elif  abs(10-x) == abs(10-y):
        result = x,y
    else:
        result = y
    return result

x = int(input('Type first number'))
y = int(input('Type second number'))

pretty_print(is_short_number(x,y))

