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
    print(symbol)

    password = []
    sym = symbol[random.randint(0,len(symbol))]
    password.append(str(random.randint(0,9)))
    password.append(sym)
    password.append((sym.upper()))
    password.append('_')
    for i in range(0,4):
        r = random.randint(0,1)
        print(r)
        if r == 0:
            password.append(sym)
        else:
            password.append(str(random.randint(0,10)))
    random.shuffle(password)
    password_string = ''.join(password)
    return password_string
result = password()
pretty_print(result)





























