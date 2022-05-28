# 5.  Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа. 

import random

def create_int_numbers_file(file_name, amount_of_numbers, min_value, max_value, separator):
    with open(file_name, 'w') as data:
        for i in range(amount_of_numbers):
            sep = separator if i != amount_of_numbers - 1 else ""
            data.write(str(random.randint(min_value, max_value)) + sep)

def number_list_from_file(file_name, separator):
    with open(file_name, 'r') as data:
        list_numbers = list(map(int, data.read().split(separator)))
    return list_numbers

def delete_odd_numbers_from_list(list_numbers):
    return  [number for number in list_numbers if number % 2 == 0]

        
def write_odd_numbers_from_list(file_name, list_numbers, separator):
    with open(file_name, 'w') as data:
        data.write(separator.join(map(str, list_numbers)))
            
file_name = 'file.txt'
file_name_odd_numbers = 'odd_file.txt'
amount_of_numbers = 10
min_value = -7
max_value = 7
separator = " "
create_int_numbers_file(file_name, amount_of_numbers, min_value, max_value, separator)
list_numbers = number_list_from_file(file_name, separator)
list_numbers = delete_odd_numbers_from_list(list_numbers)
write_odd_numbers_from_list(file_name_odd_numbers, list_numbers, separator)

