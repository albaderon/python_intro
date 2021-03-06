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
# Task 6.Создать массив из 10 элементов и проинициализировать его простыми числами в случайном порядке.
# =====================================================================================================

pretty_task(6)

def is_prime_number(number):
    upper_limit = int(math.sqrt(number))+2
    for x in range(2,upper_limit):
        if number%x==0:
            return False
    return True

prime_numbers = [x for x in range(100) if is_prime_number(x)]

random_prime_numbers = prime_numbers[:10]
random.shuffle(random_prime_numbers)

pretty_print(random_prime_numbers)