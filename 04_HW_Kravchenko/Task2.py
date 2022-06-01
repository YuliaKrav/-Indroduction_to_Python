# 2. Создать и заполнить файл случайными целыми значениями. Выполнить сортировку содержимого файла по возрастанию.

import random


def generation_of_random_numbers_list(length, min_value, max_value):
    return [random.randint(min_value, max_value) for i in range(length)]


def write_numbers_list_to_file(file_name, separator, nums_list):
    with open(file_name, 'w') as data:
        data.write(separator.join(str(element) for element in nums_list))


def read_numbers_list_from_file(file_name, separator):
    result_list = []
    with open(file_name, 'r') as data:
        result_list = list(map(int, data.read().split(separator)))
    return result_list


file_name = 'file_task_2.txt'
separator = " "
numbers_list_to_file = []
numbers_list_from_file = []


numbers_list_to_file = generation_of_random_numbers_list(
    length=10, min_value=-100, max_value=100)
write_numbers_list_to_file(file_name, separator, numbers_list_to_file)

numbers_list_from_file = read_numbers_list_from_file(file_name, separator)
# print(numbers_list_from_file)
numbers_list_from_file.sort()
write_numbers_list_to_file(file_name, separator, numbers_list_from_file)
