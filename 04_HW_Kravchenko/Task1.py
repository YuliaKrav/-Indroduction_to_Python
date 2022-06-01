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
        f'Списол {numbers_list} отсортирован по убыванию. Возрастающих последовательностей нет.')
