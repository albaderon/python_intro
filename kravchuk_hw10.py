import pretty

# Для подсчета баллов, набранных студентами группы надо обработать информацию, представленную
# в виде взаимосвязанных структур данных:
#  - group: список словарей, где словарь описывает информацию о студенте.
#  - hw_results: список с информацией о решенных д / з.
# Каждый элемент - это словарь с ключами: id студента, task_completion - список выполненных д / з.
#  - test1_results: список с информацией о решенном Test1.
# Каждый элемент - это словарь с ключами: id студента, task_completion - список выполненных заданий
#  - test1_weights: словарь с весами заданий Test1. Ключ - номер задачи, значение - вес
# задачи(кол - во баллов, которое начисляется за ее решение).
#
# Между этими данными связь устанавливается с помощью ключа студента. Например, студенту
# с id = 1024, соответствуют домашние задания и задачи из Test1, у которых ключу “id” соответствует
# значение 1024. Связь между весом задачи Test1 и ее номером устанавливается по ключу в словаре
# test1_weights.
#
# Необходимо написать 2 функции:
# - update_students_results: обновляет рейтинг студента, на основании предоставленной информации.
# См.описание ф - ции.
#  - print_students_info: распечатывает информацию о студенте, сортируя по указанному ключу из
# словаря студента. По умолчанию сортировка по ключу ‘fullname’.

pretty.pretty_task(33)

group = [
    {"id": 1024, "fullname": "Александр Скворцов",    "email": "", "github": "https://github.com/Agskvortsov", "rank": 0},
    {"id": 1025, "fullname": "Андрей Рожко",          "email": "", "github": "https://github.com/rozhkoandrew", "rank": 0},
    {"id": 1026, "fullname": "Кулишенко Алексей",     "email": "", "github": "https://github.com/", "rank": 0},
    {"id": 1027, "fullname": "Виталий Рыжков",        "email": "", "github": "https://github.com/vitalyryzhkov", "rank": 0},
    {"id": 1028, "fullname": "Гавеля Виталина",       "email": "", "github": "https://github.com/", "rank": 0},
    {"id": 1029, "fullname": "Виктор Бурлаков",       "email": "", "github": "https://github.com/SancheeZzz", "rank": 0},
    {"id": 1030, "fullname": "Виктор Горовой",        "email": "", "github": "https://github.com/lamboosanproject", "rank": 0},
    {"id": 1031, "fullname": "Надежда Симанович",     "email": "", "github": "https://github.com/simanadya", "rank": 0},
    {"id": 1032, "fullname": "Николай Марушевский",   "email": "", "github": "https://github.com/Gelios-Sky", "rank": 0},
    {"id": 1033, "fullname": "Андрей Кравчук",        "email": "", "github": "https://github.com/albaderon", "rank": 0},
    {"id": 1034, "fullname": "Шадрина Екатерина",     "email": "", "github": "https://github.com/katefeline", "rank": 0},
    {"id": 1035, "fullname": "Александр Малышев",     "email": "", "github": "https://github.com/Barabasha", "rank": 0},
    {"id": 1036, "fullname": "Владимир Веренчук",     "email": "", "github": "https://github.com/", "rank": 0}
]

hw_results = [
    {"id": 1024, "task_completion": [1,1,1,1,1,1,1,0,1,0,1,0,0,1,0,1,1,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0] },
    {"id": 1025, "task_completion": [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0] },
    {"id": 1026, "task_completion": [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] },
    {"id": 1027, "task_completion": [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0] },
    {"id": 1028, "task_completion": [1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] },
    {"id": 1029, "task_completion": [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0] },
    {"id": 1030, "task_completion": [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0] },
    {"id": 1031, "task_completion": [1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] },
    {"id": 1032, "task_completion": [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] },
    {"id": 1033, "task_completion": [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0] },
    {"id": 1034, "task_completion": [1,1,1,1,1,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] },
    {"id": 1035, "task_completion": [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0] },
    {"id": 1036, "task_completion": [1,1,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] }
]


test1_results = [
    {"id": 1024, "task_completion": [0,0,0,0,0,0,0,0,0,0,0,0] },
    {"id": 1025, "task_completion": [1,1,1,1,1,1,1,1,1,0,0,1] },
    {"id": 1026, "task_completion": [0,0,0,0,0,0,0,0,0,0,0,0] },
    {"id": 1027, "task_completion": [1,1,1,1,1,1,1,1,0,0,0,0] },
    {"id": 1028, "task_completion": [0,0,0,0,0,0,0,0,0,0,0,0] },
    {"id": 1029, "task_completion": [1,1,1,1,1,0,0,0,0,0,0,0] },
    {"id": 1030, "task_completion": [1,1,1,1,1,1,1,1,0,0,0,0] },
    {"id": 1031, "task_completion": [1,1,1,1,0,0,0,0,0,0,0,0] },
    {"id": 1032, "task_completion": [0,0,0,0,0,0,0,0,0,0,0,0] },
    {"id": 1033, "task_completion": [1,1,1,1,1,1,1,1,1,0,0,1] },
    {"id": 1034, "task_completion": [0,0,0,0,0,0,0,0,0,0,0,0] },
    {"id": 1035, "task_completion": [1,1,1,1,1,1,1,1,1,0,1,1] },
    {"id": 1036, "task_completion": [0,0,0,0,0,0,0,0,0,0,0,0] }
]

test1_weights = {
    1 : 1,
    2 : 1,
    3 : 1,
    4 : 2,
    5 : 2,
    6 : 2,
    7 : 4,
    8 : 4,
    9 : 4,
    10 : 8,
    11 : 8,
    12 : 15
}

def sum_hw_results(id):
    sum_hw_results = 0
    for dict in hw_results:
        if dict["id"] == id:
            for j in dict["task_completion"]:
                if j == 1:
                    sum_hw_results += 1
            return sum_hw_results


def sum_test1_results(id):
    sum_test1_results = 0
    for dict in test1_results:
        if dict["id"] == id:
            for i,j in enumerate(dict["task_completion"]):
                if j == 1:
                    sum_test1_results += test1_weights[i+1]
            return sum_test1_results

def update_students_results(group):
    for i, dict in enumerate(group):
        dict["rank"] = sum_hw_results(dict["id"]) + sum_test1_results(dict["id"])

    '''
    Calculate student results and put them into the student dictionary under the key "rank".
    Total rank is calculated as a sum of completed hw tasks +
        sum of completed Test1 tasks weighted proportional to its weights.
    For example, student with id=1025 has total rank = 1*32 + (1*1 + 1*1 + 1*1 + ... 1*15) = 68)
    :return: None
    '''
    pass

# def get_fullname(dict):
#     return dict.get("fullname")
#
# def get_rank(dict):
#     return dict.get("rank")


def print_card(dict):
    a = dict["github"]
    b = a.split("/")
    print(('-----------------------------------------\n'
           ': ID:               %20s:\n'
           ':.......................................:\n'
           ': Full name:        %20s:\n'
           ': Email:            %20s:\n'
           ': Github:           %20s:\n'
           ': Rank:             %20s:\n'
           '-----------------------------------------'

           ) % (dict["id"], dict["fullname"], dict["email"], b[3], dict["rank"]))


def print_students_info(group, sort_by_key="fullname"):
    for dict in sorted(group, key=lambda x : x[sort_by_key]):
        print_card(dict)


    '''
    Prints students info sorted according to the passed key in dictionary). By default, sort by students names.
    Student info should be presented as a card that includes the following information:
        - id,
        - name,
        - email,
        - github account (only name, not URL path)
        - rank
    Example (format is not strictly required):
        -----------------------------------------
        : ID:                               1025:
        :.......................................:
        : Full name:          Александр Скворцов:
        : Email:           agskvortsov@gmail.com:
        : Github:                    Agskvortsov:
        : Rank:                               42:
        -----------------------------------------
    :return: None
    '''


if __name__ == "__main__":
    update_students_results(group)
print_students_info(group, "rank")


