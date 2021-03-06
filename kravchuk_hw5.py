import math

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
# Task 18. Каждому символу в таблице символов Unicode соответствует число. Написать функцию,
# которая расчитывает сумму чисел, которые соответствуют символам, стоящим между двумя
# заданными включительно. Например, в функцию передаются символы ‘x’ и ‘z’. Значит надо
# вычислить сумму кодов символов ‘x’,’y’,’z’.
# ============================================================================================

pretty_task(18)

def sum_digit_unicod(a,b):
    x = ord(a)
    y = ord(b)+1
    sum_unicod = x
    for i in range(x,y):
        sum_unicod = sum_unicod + i
        print('symbol =', chr(i),'unicod =',i)
    return sum_unicod

a = input('Enter first symbol...')
b = input('Enter second symbol...')


result = sum_digit_unicod(a,b)
pretty_print(result)

# ============================================================================================
# Task 19. Вывести сумму всех чисел, которые являются степенью 3ки и принадлежат диапазону
# чисел от 0 до 1000000. Т.е. sum = 3^0 + 3^1 + 3^2 + ...
# ============================================================================================

pretty_task(19)

x = 0
summa = 0
exp = 0

while 0 <= exp <= 1000000:
    exp = 3**x
    if exp > 1000000:
        continue
    summa = summa + exp
    print('3 ^',x,' = ', exp)
    x = x + 1

pretty_print(summa)

# ============================================================================================
# Task 20. Вывести все числа от 0 до 1000, которые содержат в себе цифры 1 и 7.
# Т.е. числа: 17, 71, 107, 117, 127, 137, …
# ============================================================================================

pretty_task(20)

for c in range(1000):
    c = str(c)
    if '7' in c and '1' in c:
        print(c, end=', ')








