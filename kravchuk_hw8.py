import math
import random
import string

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
    symbol = string.ascii_lowercase
    symbol_up = string.ascii_uppercase
    digits = string.digits
    password = []

    password.append(str(random.choice(digits)))                           #required condition
    password.append(random.choice(symbol))                              #required condition
    password.append(random.choice(symbol_up))                           #required condition
    password.append('_')                                                #required condition
    for i in range(4):
        r = random.randint(0,2)
        if r == 0:
            password.append(random.choice(symbol))
        elif r == 1:
            password.append(random.choice(symbol_up))
        else:
            password.append(str(random.choice(digits)))
    random.shuffle(password)
    password_string = ''.join(password)
    return password_string
result = password()
pretty_print(result)





























