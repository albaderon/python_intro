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

def is_short_number(x,y,z):

    if abs(x-y) < abs(x-z):
        result = y
    elif  abs(x-y) == abs(x-z):
        result = y,z
    else:
        result = z
    return result

x = int(input('Type compare number'))
y = int(input('Type first number'))
z = int(input('Type second number'))


pretty_print(is_short_number(x,y,z))

