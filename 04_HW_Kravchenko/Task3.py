# 3.	Вот вам файл с тысячей чисел. https://cloud.mail.ru/public/DQgN/LqoQzPEec
# Задача: найти триплеты и просто выводить их на экран. Триплетом называются три числа, которые в сумме дают 0.
# (решение будет долгим, ибо является демонстрационным при теме многопоточного программирования).

def read_numbers_list_from_file(file_name, separator):
    result_list = []
    with open(file_name, 'r') as data:
        for line in data:
            result_list.append(int(line.replace(separator, "").strip()))
    return result_list


def find_and_print_triplet_brute_force_method(nums_list):
    count = 0
    for i in range(len(nums_list) - 2):
        for j in range(i + 1, len(nums_list) - 1):
            for k in range(j + 1, len(nums_list)):
                if nums_list[i] + nums_list[j] + nums_list[k] == 0:
                    print(
                        f'{nums_list[i]} + {nums_list[j]} + {nums_list[k]} = 0')
                    count += 1
    print(f'Всего триплетов - {count}')


def find_and_print_triplet_set_method(nums_list):
    count = 0
    for i in range(len(nums_list)):
        set_check_numbers = set()
        for j in range(i + 1, len(nums_list)):
            if -(nums_list[i] + nums_list[j]) in set_check_numbers:
                print(
                    f'{nums_list[i]} + {nums_list[j]} + {-(nums_list[i] + nums_list[j])} = 0')
                count += 1
            else:
                set_check_numbers.add(nums_list[j])
    print(f'Всего триплетов - {count}')


file_name = 'file_task_3.txt'
separator = "\n"
numbers_list_from_file = [-1, 2, -2, 3, -3, 1]

numbers_list_from_file = read_numbers_list_from_file(file_name, separator)
print(numbers_list_from_file)

find_and_print_triplet_brute_force_method(numbers_list_from_file)
find_and_print_triplet_set_method(numbers_list_from_file)
