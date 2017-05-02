import math
import random

def print_delim(num_repits=80):
    print('='*num_repits)
    pass

def pretty_print(value):
    print('Result =', value)
    print_delim()
    pass

def pretty_task(value):
    print_delim()
    print("Task number", value)
    pass


# ============================================================================================
# Task 21. Вывести на экран все простые числа от 1 до 100
# ============================================================================================

pretty_task(21)

def is_prime_number(a,b):
    lower_limit = a
    upper_limit = b
    for i in range(lower_limit,upper_limit+1):
        sum_division = 0
        for x in range(lower_limit,i+1):
            if i%x==0:
                sum_division = sum_division + 1
                # print(i,x,sum_division)
        if sum_division < 3:
            print('Prime number:', i)

is_prime_number(1,100)

# ============================================================================================
# Task 22. Создать функцию, выводящую на экран случайно сгенерированное
# 12 ти-значное натуральное число и возвращающую его наибольшую цифру.
# ============================================================================================

pretty_task(22)
def twalve_digit_num(a):
    lower_limit = 10**(a-1)
    upper_limit = 10**a
    number = random.randint(lower_limit,upper_limit)
    max_digit = 0
    for i in str(number):
        if int(i) > max_digit:
            max_digit = int(i)
    return number, max_digit

number, max_digit = twalve_digit_num(12)
print('Twalve digit number = %d Max digit = %d' %
             (number, max_digit))

# ============================================================================================
# Task 23. Вычислить факториал некоторого числа, используя рекурсию.
# ============================================================================================

pretty_task(23)

def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

factorial = factorial(5)
print('Factorial from 5 =',factorial)

# ============================================================================================
# Task 24. Случайным образом программа выбирает целое число от 1 до 10
# и предлагает пользователю его угадать. Пользователь вводит число,а программа
# проверяет его и, если пользователь не угадал, то говорит больше или меньше.
# После чего опять просит угадать. И так пока пользователь не угадает
# выбранное число.
# ============================================================================================

pretty_task(24)

random = random.randint(1,10)
print(random)


while True:
    enter_number = int(input('Guess the number from 1 to 10...'))
    if enter_number > 10 or enter_number < 1:
        print('Your chose from 1 to 10, enter again...')
    elif enter_number < random:
        print('more')
    elif enter_number > random:
        print('less')
    else:
        print('Bingo!!!')
        break

