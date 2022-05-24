# Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 

#numbers_list = []
numbers_list = [2, 3, 4, 5, 6]
#numbers_list = [2, 3, 5, 6]

last_i = len(numbers_list) // 2 if  len(numbers_list) % 2 == 0 else len(numbers_list) // 2 + 1
result_list = []

for i in range(last_i):
    result_list.append(numbers_list[i] * numbers_list[len(numbers_list) - 1 - i])


print(result_list)