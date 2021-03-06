# Task 7. Преобразовать строку с американским форматом даты в европейский.
# Например, "05.17.2016" преобразуется в "17.05.2016"

date_us = '05.17.2016'
idx1 = date_us.find('.')            # Find 1st idx
idx2 = date_us.find('.',idx1+1)     # Find 2nd idx
curr_month = date_us[:idx1]         # Month
curr_day = date_us[idx1+1:idx2]     # Day
curr_year = date_us[idx2+1:]        # Year
date_eu = curr_day + '.' + curr_month + '.' + curr_year
print('----------------------------------------------------------------------------------------------------------------')

print('Result task 1 :', date_us, 'with an American date format is transformed to'
      ,date_eu, 'with an Europe date format')
print('----------------------------------------------------------------------------------------------------------------')

#========================================================================================
#========================================================================================

# Task 8. Написать программу, которая берет две строки и помещает первую строку
# в середину второй. Результат помещается в середину первой. Длину строки можно
# получить с помощью функции len().

first_str = '11111111'
second_str = '0000000'
idx_middle_f = int(len(first_str)//2)    # Index of middle ferst string
idx_middle_s = int(len(second_str)//2)   # Index of middle second string
program_1 = second_str[:idx_middle_s] + first_str + second_str[idx_middle_s:]
program_2 = first_str[:idx_middle_f] + program_1 + first_str[idx_middle_f:]

print('Result task 2 : If first string is', first_str, 'and second string is', second_str,
      ' it turns out', program_2)
print('----------------------------------------------------------------------------------------------------------------')

#========================================================================================
#========================================================================================

# Task 9. Написать программу, которая переводит в верхний регистр второе слово
# (слово - последовательность символов между двумя пробелами).
# Например: “abc def ghj” -> “abc DEF ghj”

curr_word = 'abc def ghj'
idx_wd1 = curr_word.find(' ')              # Index the first " "
idx_wd2 = curr_word.find(' ', idx_wd1+1)   # Index the second " "
middle_w = curr_word[idx_wd1+1:idx_wd2]    # The middle word
program_w = curr_word[:idx_wd1] + ' ' + middle_w.upper() +' ' + curr_word[idx_wd2+1:]

print('Result task 3 :', '"' + curr_word + '"','transformed to','"' + program_w + '"')
print('----------------------------------------------------------------------------------------------------------------')

#========================================================================================
#========================================================================================

# Task 10. Дана строка вида "Leo Tolstoy*1828-08-28*1910-11-20". В этой строке
# указаны имя писателя и через символ * даты рождения и смерти. Даты указаны в
# формате "YYYY-MM-DD". Требуется написать программу, которая по переданной строке
# определит возраст писателя и вернет его имя и возраст. Например, для строки
# "Leo Tolstoy*1828-08- 28*1910-11-20" функция должна вернуть: "Leo Tolstoy", 82

str_writer = 'Leo Tolstoy*1828-08-28*1910-11-20'
idx_wr1 = str_writer.find('*')                 # Index ferst "*"
idx_wr2 = str_writer.find('*', idx_wr1 +1)     # Index second "*"
idx_wr3 = str_writer.find('-')                 # Index ferst "-"
idx_wr4 = str_writer.find('-', idx_wr2)        # Index ferst "-"
program_year_old = int(str_writer[idx_wr2+1:idx_wr4]) - int(str_writer[idx_wr1+1:idx_wr3])

print('Result task 4 :', '"' + str_writer[:idx_wr1] + '",', program_year_old )
print('----------------------------------------------------------------------------------------------------------------')

#========================================================================================
#========================================================================================











