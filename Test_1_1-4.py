import math
import random
import string

def print_delim(num_repits=80):
    print('='*num_repits)


def pretty_print(value):
    print('Result:', value)
    print_delim()


def pretty_task(value):
    print_delim()
    print("Task number", value)


# ============================================================================================
# Task 1. (a + b * c)^2
# Task 2.  a - 4 * b / c
# Task 3. (a * b + 4) / (c - 1)
# ============================================================================================

pretty_task('1-3')

def three_variables():
    a = int(input('Type value of a...'))
    b = int(input('Type value of b...'))
    c = int(input('Type value of c...'))
    result_1 = (a + b * c) ** 2
    if c == 0:
        result_2 = 'Division by zero error'
    else:
        result_2 = a - 4 * b / c
    if c == 1:
        result_3 = 'Division by zero error'
    else:
        result_3 = (a * b + 4) / (c - 1)
    return result_1, result_2, result_3

a,b,c = three_variables()
pretty_print('\n(a + b * c)^2 = %s \n a - 4 * b / c = %s \n(a * b + 4) / (c - 1) = %s'
             % (a,b,c))

# ============================================================================================
# Task 4. Найти произведение нечетных цифр пятизначного целого числа, введенного пользователем
# с клавиатуры.
# ============================================================================================

pretty_task(4)

def mult_odd_numbers():
    mult = 1
    while mult:
        five_digit_number = input('Type integer five digit number')
        if not five_digit_number.isdigit():
            print('number is not digit')
            continue
        elif len(five_digit_number) != 5:
            print('It is not five digit number')
            continue
        else:
            for i in range(5):
                elem = int(five_digit_number[i])
                if elem%2 == 0:
                    continue
                else:
                    mult *= elem
        return mult


pretty_print(mult_odd_numbers())