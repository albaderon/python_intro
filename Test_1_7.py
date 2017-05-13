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
# Task 7.Найти сумму десяти первых чисел ряда Фибоначчи.
# =====================================================================================================

pretty_task(7)

fibonacci_list = [1,1]
sum_fib = 0
for i in range(2,10):
    sum_fib = fibonacci_list[i-1]+fibonacci_list[i-2]
    fibonacci_list.append(sum_fib)
print(fibonacci_list)
sum_fib = sum(fibonacci_list)
pretty_print(sum_fib)
