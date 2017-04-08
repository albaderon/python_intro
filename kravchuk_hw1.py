#=================================================================================
# Test commit

import math # Import mathematical functions

a = int(input("Input value a="))   # The value of "a"
b = int(input("Input value b="))   # The value of "b"
c = int(input("Input value c="))   # The value of "c"

#=================================================================================

# Task 1. Найти результат выражения для произвольных значений a,b,c:
#  a + b * ( c / 2 )

result = a + b * (c / 2)  #Formula
print("1.For arbitrary values a = %d, b = %d, c = %d result of expression = %.2f" %
        (a, b, c, result))

#=================================================================================

# Task 2. Найти результат выражения для произвольных значений a,b:
#  (a**2 + b**2) % 2

result = (a**2 + b**2) % 2 #Formula
print("2.For arbitrary values a = %d, b = %d result of expression = %d" %
        (a, b, result))

#=================================================================================

# Task 3. Найти результат выражения для произвольных значений a,b,c:
#  ( a + b ) / 12 * c % 4 + b

result = (a + b) / 12 * c % 4 + b  #Formula
print("3.For arbitrary values a = %d, b = %d, c = %d result of expression = %.2f" %
        (a, b, c, result))

#=================================================================================

#Task 4. Найти результат выражения для произвольных значений a,b,c:
#  (a - b * c ) / ( a + b ) % c

result = (a - b * c ) / ( a + b ) % c  #Formula
print("4.For arbitrary values a = %d, b = %d, c = %d result of expression = %.2f" %
        (a, b, c, result))

#=================================================================================

#Task 5. Найти результат выражения для произвольных значений a,b,c:
#  | a - b | / ( a + b )3 - cos(c)

result =  math.fabs(a - b) / ( a + b ) ** 3 - math.cos(c)  #Formula
print("5.For arbitrary values a = %d, b = %d, c = %d result of expression = %.2f" %
        (a, b, c, result))

#=================================================================================

#Task 6. Найти результат выражения для произвольных значений a,b,c:
#  ( ln( 1 + c ) / -b )4+ | a |

result =  ( math.log(1 + c) / (-b) ) ** 4 + math.fabs(a)  #Formula
print("6.For arbitrary values a = %d, b = %d, c = %d result of expression = %.2f" %
        (a, b, c, result))