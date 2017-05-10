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
# Task 31. 1.Создать генератор паролей, который будет генерировать случайные неповторяющиеся
# пароли по следующим правилам:
# --- Пароль состоит из 8 символов
# --- В пароле допускаются только латинские большие и маленькие буквы, цифры и символ подчеркивания
# --- Пароль обязательно должен содержать Большие и маленькие буквы и цифры
# ============================================================================================

pretty_task(31)

def password():
    symbol = [chr(x) for x in range(97,123)]
    symbol_up = [chr(c) for c in range(65,91)]
    password = []

    password.append(str(random.randint(0,9)))                           #required condition
    password.append(symbol[random.randint(0,(len(symbol)-1))])          #required condition
    password.append(symbol_up[random.randint(0,(len(symbol_up)-1))])    #required condition
    password.append('_')                                                #required condition
    for i, elem in enumerate(range(0,4)):
        r = random.randint(0,2)
        if r == 0:
            password.append(symbol[random.randint(0,(len(symbol)-1))])
        elif r == 1:
            password.append(symbol_up[random.randint(0,(len(symbol_up)-1))])
        else:
            password.append(str(random.randint(0,10)))
    random.shuffle(password)
    password_string = ''.join(password)
    return password_string
result = password()
pretty_print(result)





























