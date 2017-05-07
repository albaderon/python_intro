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

def random_list(num, lower_imit, upper_limit):
    lst = []
    for i in range(num):
        lst.append(random.randint(lower_imit,upper_limit))
    return lst

lst1 = random_list(10,0,100)

# ============================================================================================
# Task 25. Написать функцию для поиска среднее арифметическое всех элементов списка.
# ============================================================================================

pretty_task(25)

def average_list(lst):
    sum = 0
    for i in lst:
        sum += i
    average = sum / len(lst)
    print(lst)
    return average

pretty_print(average_list(lst1))

# ============================================================================================
# Task 26. Написать функцию для поиска разницы сумм всех четных и всех нечетных чисел
# списка. Т.е. От суммы четных чисел вычесть сумму нечетных чисел в списке.
# ============================================================================================

pretty_task(26)

def different_sum_list(lst):
    sum_even = 0
    sum_odd = 0
    for i in lst:
        if i%2 == 0:
            print('even',i)
            sum_even += i
        else:
            print('odd',i)
            sum_odd += i
    dif_sum = sum_even - sum_odd
    return dif_sum

pretty_print(different_sum_list(lst1))

# ============================================================================================
# Task 27. Создайте список на 50 элементов из всех нечётных чисел от 1 до 99,
# выведите его на экран в строку, а затем этот же список выведите на экран
# тоже в строку, но в случайном порядке (например, 99 11 43 19 … 7 91 3 1).
# ============================================================================================

pretty_task(27)

lst = []

for i, elem in enumerate(range(1,100,2)):
    lst.append(elem)
    lst[i] = random.randint(0,50)

# random.shuffle(lst)

pretty_print(lst)

# ============================================================================================
# Task 28. Создайте 2 списка из 5 случайных целых чисел из отрезка [0;5]
# каждый, выведите списки на экран в двух отдельных строках. Посчитайте
# среднее арифметическое элементов каждого списка и сообщите, для какого
# из списков это значение оказалось больше (либо сообщите, что их средние
# арифметические равны).
# ============================================================================================

pretty_task(28)

def average_different_list():

    first_list = random_list(5,0,5)
    second_list = random_list(5,0,5)

    first_average = average_list(first_list)
    print(first_average)
    second_average = average_list(second_list)
    print(second_average)

    if first_average > second_average:
        result = 'Average of first random list more'
    elif second_average > first_average:
        result = 'Average of second random list more'
    else:
        result = 'Averages are equal'
    return result

pretty_print(average_different_list())

# ============================================================================================
# Task 29. Создайте список из 11 случайных целых чисел из отрезка [-1;1],
# выведите список на экран в строку. Определите какой элемент встречается
# в списке чаще всего и выведите об этом сообщение на экран. Если два
# каких-то элемента встречаются одинаковое количество раз, то не выводить
# ничего.
# ============================================================================================

pretty_task(29)

def often_values():
    lst4 = random_list(11,-1,1)
    print(lst4)
    sum_often_one = 0
    sum_often_zero = 0
    sum_often_unone = 0
    for i in range(len(lst4)):
        if lst4[i] == 1:
            sum_often_one += 1
        elif lst4[i] == -1:
            sum_often_unone += 1
        else:
            sum_often_zero +=1
    if sum_often_one > sum_often_unone and sum_often_one > sum_often_zero:
        result = '1 often'
    elif sum_often_zero > sum_often_one and sum_often_zero > sum_often_unone:
        result = '0 often'
    elif sum_often_unone > sum_often_zero and sum_often_unone > sum_often_one:
        result = '-1 often'
    else:
        result = ''
    return result

pretty_print(often_values())

# ============================================================================================
# Task 30. Создать программу, которая запрашивает у пользователя
# произвольную строку символов. Далее программа ее шифрует и выводит
# на экран в зашифрованном виде. Шифрование происходит путем замены
# каждого символа символом, который находится на 5 позиций правее в
# предопределенной таблице шифрования. Таблица шифрования задается
# программистом в виде одномерного списка символов. Если при выборе
# символа для шифровки таблица шифрования заканчивается, то циклически
# переходить к ее началу.
# Например: Таблица шифрования (а,б,в,г,д,о,1,2,3,4,5,6,-,0)
# Исходная строка, которую ввел пользователь: год-2016
# Зашифрованная строка, которую выдала программа: 354г-д6в
# Примечание: т.н. таблица шифрования может быть представлена как строка
# или список.
# ============================================================================================

pretty_task(30)

def encryption():
    enter_string = input('Enter string...')
    encryption_table = ['а','б','в','г','д','о','1','2','3','4','5','6','-','0']
    encryption_lst = []

    for i in range(len(enter_string)):
        encryption_lst.append(enter_string[i])  #string2list
        replace_index = encryption_table.index(encryption_lst[i])
        replace_symbol = encryption_table[(replace_index + 5) % len(encryption_table)]
        encryption_lst[i] = replace_symbol
        # encryption_lst.insert(i,encryption_table[4+i])
    encryption_str = ''.join(encryption_lst)    #list2string

    return encryption_str

pretty_print(encryption())






































