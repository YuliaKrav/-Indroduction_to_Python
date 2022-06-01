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
