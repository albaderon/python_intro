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
# Task 11.В двумерном массиве отсортировать четные столбцы по возрастанию, а нечетные - по убыванию
# =====================================================================================================

pretty_task(11)

table = [[10,11,12,13,14,15,16,17],
         [21,22,23,24,25,26,27,28],
         [31,32,33,34,35,36,37,38]]

def print_table(table):
    for line in table:
        for elem in line:
            print(elem, end='\t')
        print()

print_table(table)
print()


def transposed_matrix(table):
    len_table = len(table)
    len_line = len(table[0])


    transposed_matrix = [[0 for x in range(len_table)] for x in range(len_line)]



    for idx1_tb2, line_tb2 in enumerate(transposed_matrix):
        for idx2_tb2, elem_tb2 in enumerate(line_tb2):
            transposed_matrix[idx1_tb2][idx2_tb2] = table[idx2_tb2][idx1_tb2]

    return transposed_matrix

def sort_matrix(table):
    sort_table = transposed_matrix(table)
    for i, elem in enumerate(sort_table):
        if i%2==0:
            sort_table[i].sort()
        else:
            sort_table[i].sort(reverse=True)
    return transposed_matrix(sort_table)


print_table(sort_matrix(table))



