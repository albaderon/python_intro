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
# Task 12.Для проверки остаточных знаний учеников после летних каникул, учитель младших классов решил
# начинать каждый урок с того, чтобы задавать каждому ученику пример из таблицы умножения, но в классе
# 15 человек, а примеры среди них не должны повторяться. В помощь учителю напишите программу, которая
# будет выводить на экран 15 случайных примеров из таблицы умножения (от 2*2 до 9*9, потому что задания
# по умножению на 1 и на 10 — слишком просты). При этом среди 15 примеров не должно быть повторяющихся
# (# примеры 2*3 и 3*2 и им подобные пары считать повторяющимися)
# =====================================================================================================

pretty_task(12)
numbers = [x for x in range(2,10)]
examples = []
examples_one_day = []
for x in range(8):
    for i in range(0,len(numbers)):
        example = str(numbers[0])+'*'+str(numbers[i])
        examples.append(example)
    numbers.remove(numbers[0])

while len(examples_one_day) != 15:
    r = random.choice(examples)
    if r not in examples_one_day:
        examples_one_day.append(r)

print(examples_one_day)
