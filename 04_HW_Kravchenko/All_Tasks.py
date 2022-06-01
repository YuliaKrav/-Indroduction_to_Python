# 1.	Дан список чисел. Создать список, в который попадают числа, описываемые возрастающую последовательность.
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д. Порядок элементов менять нельзя

def is_list_in_descending_order(nums_list):

    nums_list_in_descending_order = nums_list.copy()
    nums_list_in_descending_order.sort(reverse=True)

    return (nums_list == nums_list_in_descending_order)


def find_first_index_of_new_sequence(nums_list):
    number_index = 0

    while number_index < len(nums_list) - 1 and nums_list[number_index] >= numbers_list[number_index + 1]:
        number_index += 1

    return number_index


def create_ascending_list(nums_list, first_index):
    result_list = [nums_list[first_index]]

    for i in range(first_index + 1, len(nums_list)):
        if result_list[-1] < nums_list[i]:
            result_list.append(numbers_list[i])

    return result_list


# numbers_list = [- 2, 7, 7, 8, 6, 6, 5, 5, 10, 4, 3, 2, 1, 11]
numbers_list = [1, 5, 2, 3, 4, 6, 1, 7]


if not is_list_in_descending_order(numbers_list):
    print(f'В списке {numbers_list} одна из возрастающих последовательностей - {create_ascending_list(numbers_list, find_first_index_of_new_sequence(numbers_list))}')
else:
    print(
        f'Список {numbers_list} отсортирован по убыванию. Возрастающих последовательностей нет.')

#*******************************************************************************************************************************************
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

#*******************************************************************************************************************************************
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


#*******************************************************************************************************************************************

# Экстра-задачи:
# 1.	Давайте представим, что ваша компания только что наняла вашего друга из колледжа и заплатила вам реферальный бонус. Потрясающе!
# Чтобы отпраздновать, вы берете свою команду в очень странный бар по соседству и используете реферальный бонус, чтобы купить и построить
# самую большую трехмерную пирамиду из пивных банок, которую вы можете.
# Пирамида пивных банок будет квадратировать количество банок на каждом уровне - 1 банка на верхнем уровне, 4 на втором, 9 на следующем, 16, 25...
# Определите функцию beeramid, чтобы вернуть количество полных уровней пирамиды пивных банок, которую вы можете сделать, учитывая параметры:
# реферальный бонус и цена пивной банки.
# Например:
# beeramid(1500, 2)# 12
# beeramid(5000, 3)# 16

def beeramid(bonus, price_per_can):
    amount_of_cans = bonus // price_per_can

    amount_of_lines = 0
    while ((amount_of_lines * (amount_of_lines + 1) * (2 * amount_of_lines + 1)) / 6) <= amount_of_cans:
        amount_of_lines += 1

    return amount_of_lines - 1


bonus = 1500
price_per_can = 2

# bonus = 5000
# price_per_can = 3

print(f'При бонусе = {bonus} и цене за банку = {price_per_can} количество полных уровней в пирамиде = {beeramid(bonus, price_per_can)}')

#*******************************************************************************************************************************************

# 2.	Создать функцию, которая из списка чисел возвращает число, являющее суммой двух или нескольких других элементов,
# либо возвращающее None, если такого числа нет.

# Примечание, все дубли сумм удаляются, например 8 = 3 + 5, 8 = 5 + 3 - останется только 8 = 3 + 5
def create_possible_lists(nums_list, number, result_list, nums_part_list=[]):
    total = sum(nums_part_list)

    # print(f'total = {total}, number = {number}, nums_part_list = {nums_part_list}, nums_list = {nums_list}')
    if total == number:
        # print(f'{number} = sum({nums_part_list})')
        nums_part_list.sort()
        if nums_part_list not in result_list:
            result_list.append(nums_part_list)

    if len(nums_list) <= 0:
        return

    for i in range(len(nums_list)):
        create_possible_lists(
            nums_list[i + 1:], number, result_list, nums_part_list + [nums_list[i]])


numbers_list = [1,  -4, 3, 2, 4, 1, 1, 6, 7]
# numbers_list = [1, 4, -1, 3, 2]
# numbers_list = [2, 1, -1]
# numbers_list = [8, 3, 1, 5, 4, 4, -4]
# numbers_list = [8, 3, 1]

possible_copmonents_list = []

for element in set(numbers_list):
    numbers_list_copy = numbers_list.copy()
    while element in numbers_list_copy:
        numbers_list_copy.remove(element)
    create_possible_lists(numbers_list_copy, element, possible_copmonents_list)

if len(possible_copmonents_list) == 0:
    print('None - чисел являющихся суммой других элементов в списке нет.')
else:
    numbers_with_components_set = {sum(element)
                                   for element in possible_copmonents_list}
    print(
        f'Числа в списке {numbers_list}, не являющиеся суммой друших элеменнтов - {set(numbers_list) - numbers_with_components_set}')
    print(f'Возможные комбинации для оставшихся чисел:')
    for element in possible_copmonents_list:
        print(f'{sum(element)} = sum({element})')
    # print(len(possible_copmonents_list))

#*******************************************************************************************************************************************

# 3.	Вот вам задача: https://cloud.mail.ru/public/7X6f/PXza5yoTP
# Вам помогут знания со второй лекции. Решение в лоб (скопировать число, вставить в переменную, сделать из нее список с числами) – слабо подойдет.
# Подумайте, как то, что было в лекции, вяжется с этой задачей.

file_name = "file_task_add_3.txt"

sum = 0

with open(file_name, 'r') as data:
    for line in data:
        sum += int(line[: -1])

print(f'Первые 10 цифр суммы всех чисел из файла = {str(sum)[0 : 10]}')

#*******************************************************************************************************************************************
