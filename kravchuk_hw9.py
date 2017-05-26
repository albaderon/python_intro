import math
import random
import string
import pickle

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

# =========================================================================================================
# Task 32.В программе phone_book реализовать следующие функции:
# - find_entry_age_phonebook         # найти все записи с указанным возрастом
# - print_phonebook_by_age           # распечатать все записи отсортированные по возрасту
# - delete_entry_name_phonebook      # удалить все записи с указанным именем
# - avr_age_of_all_persons           # распечатать средний возраст всех абонентов
# - increase_age                     # увеличить возраст всем абонентам на заданное пользователем кол-во лет
# - <ваша_функция>                   # добавить любую функцию, манипулирующую записями (печать, добавление,
#                                    удаление) в телефонной книге на ваше усмотрение.
# - добавить поддержку еще одного поля (например, скайп, адрес, день рождения) и сделайте по нему поиск и
# печать. Т.е. добавить функцию для поиска и обновить существующую функцию печати.
# При выполнении обратите внимание на обработку ошибок. Например, если при удалении записи с заданным
# именем нет, то вывести сообщение “Not found!”.
# ==========================================================================================================

pretty_task(32)



phone_book = [
              {"name": "Petr", "surname": "Petrov", "age": 50, "phone_number":"+380501234567"},
              {"name": "Ivan", "surname": "Ivanov", "age": 15, "phone_number":"+380507654321"},
             ]

def print_entry(number, entry):
    print ("--[ %s ]--------------------------" % number)
    print ("| Surname: %20s |" % entry["surname"])
    print ("| Name:    %20s |" % entry["name"])
    print ("| Age:     %20s |" % entry["age"])
    print ("| Skype:   %20s |" % entry.get("Skype", "No Skype"))


    print ()

def get_name(dict):
    return dict["name"]

def get_surname(dict):
    return dict["surname"]

def print_phonebook():
    print ()
    print ()
    print ("#########  Phone book  ##########")
    print ()

    phone_book.sort(key=get_name)

    number = 1
    for entry in phone_book:
        print_entry(number, entry)
        number += 1

def print_phonebook_by_surname():
    print ()
    print ()
    print ("#########  Phone book  ##########")
    print ()

    phone_book.sort(key=get_surname)

    number = 1
    for entry in phone_book:
        print_entry(number, entry)
        number += 1
        found = True


def get_age(dict):
    return dict["age"]

def get_skype(dict):
    return dict["Skype"]

def print_phonebook_by_skype():
    print()
    print()
    print("#########  Phone book  ##########")
    print()

    number = 1
    phone_book.sort(key=get_skype)

    for entry in phone_book:
        print_entry(number, entry)
        number += 1

def print_phonebook_by_age():
    print()
    print()
    print("#########  Phone book  ##########")
    print()

    number = 1
    phone_book.sort(key=get_age)

    for entry in phone_book:
        print_entry(number, entry)
        number += 1

def add_entry_phonebook(surname, name, age):
    entry = {}
    entry["surname"] = surname
    entry["name"] = name
    entry["age"] = age
    phone_book.append(entry)

def printError(message):
    print ("ERROR: %s" % message)

def printInfo(message):
    print ("INFO: %s" % message)

def find_entry_name_phonebook(name):
    idx = 1
    found = False
    for entry in phone_book:
        if entry["name"] == name:
            print_entry(idx, entry)
            idx += 1
            found = True
    if not found:
        printError("Not found!!")

def find_phonebook_by_skype(skype):
    found = False
    for entry in phone_book:
        if entry.get("Skype", "No Skype") == skype:
            print_entry(1, entry)
            found = True
    if not found:
        printError("Not found!!")

def find_entry_age_phonebook(age):
    idx = 1
    found = False
    for entry in phone_book:
        if entry["age"] == age:
            print_entry(idx, entry)
            idx += 1
            found = True
    if not found:
        printError("Not found!!")


def avr_age_of_all_persons():
    sum_age = 0
    for entry in phone_book:
        sum_age += entry["age"]
    avr_age = sum_age/len(phone_book)
    print("Average age of person: %d" % avr_age)

def delete_entry_name_phonebook(name):
    found = False
    for entry in phone_book:
        if entry["name"] == name:
            phone_book.remove(entry)
            found = True
    if not found:
        printError("Not found!!")

def count_all_entries_in_phonebook():
    print ("Total number of entries: ", len(phone_book))

def increase_age(number_of_years):
    for i, entry in enumerate(phone_book):
        phone_book[i]["age"] += number_of_years
    print_phonebook_by_age()

def add_skype(name):
    found = False
    for i, entry in enumerate(phone_book):
        if phone_book[i]["name"] == name:
            skype = str(input("    Enter Skype: "))
            phone_book[i]["Skype"] = skype
            found = True
    if not found:
        printError("Not found!!")

def save_to_file():
    pickle.dump(phone_book, open("phone_book.save", "wb"))
    printInfo("Phonebook is saved into 'phone_book.save'")


def load_from_file():
    global phone_book
    phone_book = pickle.load(open("phone_book.save", "rb"))
    printInfo("Phonebook is loaded from 'phone_book.save'")


def main():
    while True:
        user_input = ""
        try:
            print ()
            print ()
            print ()
            print ("~ Welcome to phonebook ~")
            print ("Select one of actions below:")
            print ("     1 - Print phonebook entries")
            print ("     2 - Print phonebook entries (by age)")
            print ("     3 - Add new entry")
            print ("     4 - Find entry by name")
            print ("     5 - Find entry by age")
            print ("     6 - Delete entry by name")
            print ("     7 - The number of entries in the phonebook")
            print ("     8 - Avr. age of all persons")
            print ("     9 - Increase age by num. of years")
            print ("     10 - Print phonebook entries (by surname)")
            print ("     11 - Add Skype")
            print ("     12 - Find phonebook entries (by Skype)")
            print ("-----------------------------")
            print ("     s - Save to file")
            print ("     l - Load from file")
            print ("     0 - Exit")

            user_input = input("Enter you choice: ")
            choice = int(user_input)

            if choice == 1:
                print_phonebook()
            elif choice == 2:
                print_phonebook_by_age()
            elif choice == 3:
                surname = str(input("    Enter surname: "))
                name = str(input("    Enter name: "))
                age = int(input("    Enter age: "))
                add_entry_phonebook(surname, name, age)
            elif choice == 4:
                name = str(input("    Enter name: "))
                find_entry_name_phonebook(name)
            elif choice == 5:
                age = int(input("    Enter age: "))
                find_entry_age_phonebook(age)
            elif choice == 6:
                name = str(input("    Enter name: "))
                delete_entry_name_phonebook(name)
            elif choice == 7:
                count_all_entries_in_phonebook()
            elif choice == 8:
                avr_age_of_all_persons()
            elif choice == 9:
                nmbrs_of_years = int(input("    Enter number of years to add to current ages: "))
                increase_age(nmbrs_of_years)
            elif choice == 10:
                print_phonebook_by_surname()
            elif choice == 11:
                name = str(input("    Enter name who add Skype: "))
                add_skype(name)
            elif choice == 12:
                skype = str(input("    Enter skype: "))
                find_phonebook_by_skype(skype)
            elif choice == 0:
                print ("Bye!")
                break
            else:
                print ("Enter action within range [0..11]")

        except ValueError:
            if str(user_input) == 's':
                save_to_file()
            elif str(user_input) == 'l':
                load_from_file()
            else:
                printError("Something went wrong. Try again...")


if __name__ == '__main__':
    main()

















