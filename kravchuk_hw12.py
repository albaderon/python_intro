import pretty
import random
import math

# Task 35. Создать два класса: Окружность и Точка. Создать в классе окружности метод,
# который принимает в качестве параметра точку и проверяет находится ли данная точка
# внутри окружности.

pretty.pretty_task(35)

class Circle:

    def __init__(self, x=0,y=0,r=0):
        self.x = x
        self.y = y
        self.r = r


    def is_point_in_circle(self):

        if ((point.x-self.x)**2 + (point.y-self.y)**2) <= self.r**2:
            return True
        else:
            return False





class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y


circle = Circle(5,5,5)
point = Point(3,2)

print(circle.is_point_in_circle())

