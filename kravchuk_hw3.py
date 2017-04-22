import math

def print_delim(num_repits=40):
    print('\u263a'*num_repits + ' ' '\u2b57' + ' ' + '\u263a'*num_repits)
    pass

def pretty_print(value):
    print('Result =', value)
    print_delim()
    pass

def pretty_task(value):
    print_delim()
    print("Task number ", value)
    pass


# ============================================================================================
# Task 11. Написать функцию, которая будет переводить градусы в радианы.
# Используя эту функцию вывести на экран значения косинусов углов в 60, 45 и 40 градусов.
# ============================================================================================
pretty_task(11)

def degree2radian(degree):
    radian = degree * math.pi / 180
    return radian

def cos_task(dgr):
    cos = math.cos(degree2radian(dgr))
    return cos

dr1 = 60
dr2 = 45
dr3 = 40

print('Result = %.2f, %.2f, %.2f' % (cos_task(dr1), cos_task(dr2), cos_task(dr3)))
print_delim()
# ============================================================================================
# Task 12. Написать функцию, которая рассчитывает сумму всех цифр некоторого
# трехзначного числа, введенного пользователем в консоли, без использования операторов цикла.
# ============================================================================================

pretty_task(12)

def amount(number):
    hundreds = number // 100
    dozens = (number - hundreds * 100)//10
    units = number % 10
    sum_td = hundreds+dozens+units
    return sum_td


number_3 = int(input('Enter three-digit number... '))

result = amount(number_3)

pretty_print(result)

# ============================================================================================
# Task 13. Пользователь вводит длины катетов прямоугольного треугольника. Написать функцию,
# которая вычислит и выведет на экран площадь треугольника и его периметр.
# ============================================================================================

pretty_task(13)

a = int(input('Enter side a... '))
b = int(input('Enter side b... '))

def square_perimeter(x,y):
    square = x*y/2
    perimeter = x+y+(math.sqrt(x**2 + y**2))
    return square, perimeter

square, perimeter = square_perimeter(a,b)

pretty_print('Square = %.2f Perimeter = %.2f' % (square, perimeter))





