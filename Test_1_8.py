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
# Task 8.В одномерном массиве поменять местами минимальный и максимальный элементы.
# Остальные оставить на своих местах.
# =====================================================================================================

pretty_task(8)

lst = [random.randint(0,100) for x in range(10)]
print(lst)
max_elem_list = max(lst)
min_elem_list = min(lst)
idx_max_elem = lst.index(max_elem_list)
idx_min_elem = lst.index(min_elem_list)
lst.remove(max_elem_list)
lst.remove(min_elem_list)
lst.insert(idx_min_elem,max_elem_list)
lst.insert(idx_max_elem,min_elem_list)
print('Max:', max_elem_list)
print('Min:', min_elem_list)
print(lst)


