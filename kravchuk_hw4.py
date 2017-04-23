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
# Task 14. Написать функцию, которая будет проверять четность некоторого числа.
# ============================================================================================

pretty_task(14)

def is_number_even(number):
    return not number % 2

    # result = number % 2
    # if result == 0:
    #     return True
    # else:
    #     return False

num_val = int(input('Enter number... '))
pretty_print(is_number_even(num_val))

# ============================================================================================
# Task 15. Написать функцию, которая отвечает на вопрос, пересекаются ли две заданные
# окружности на плоскости. Каждая окружность задается координатами центра и радиусом.
# ============================================================================================

pretty_task(15)

circle_x1 = 0
circle_y1 = 0
circle_r1 = 3

circle_x2 = 5
circle_y2 = 0
circle_r2 = 1

def is_circles_cross(x1,y1,r1,x2,y2,r2):
    a = math.fabs(x1 - x2)
    b = math.fabs(y1 - y2)
    c = math.sqrt(a**2 + b**2)
    if c > (r1+r2) or x1!=x2 and y1!=y2 and r1!=r2 or c<(math.fabs(r1-r2)):
        return False
    else:
        return True


pretty_print(is_circles_cross(circle_x1,circle_y2,circle_r1,circle_x2,circle_y2,circle_r2))

# ============================================================================================
# Task 16. Два поезда движутся на скорости V1 и V2 навстречу друг другу.
# Между ними 10 км. пути. Через 4 км пути первый поезд может свернуть на запасной путь.
# При заданных скоростях узнать столкнутся ли поезда.

# ============================================================================================

pretty_task(16)

train_v1 = 50
train_v2 = 70

def is_damage(v1,v2):
    if 4/v1 > (10-4)/v2:
        return True
    else:
        return False
    # return not 4/v1 < (10-4)/v2

pretty_print(is_damage(train_v1,train_v2))

# ============================================================================================
# Task 17. Написать функцию решения квадратного уравнения.
# ============================================================================================

pretty_task(17)

def quadratic_equation(a,b,c):
        d=b**2-4*a*c
        if  d > 0:
            x1=(-b+math.sqrt(d))/2*a
            x2=(-b-math.sqrt(d))/2*a
            return x1,x2

        elif d == 0:
            x1=-b/2*a
            return x1,None

        else:
            return None,None

a = int(input('Enter a... '))
b = int(input('Enter b... '))
c = int(input('Enter c... '))

x1,x2 = quadratic_equation(a,b,c)

pretty_print("Equation with a=%d, b=%d, c=%d has roots: %s, %s" % (a, b, c, x1, x2))







