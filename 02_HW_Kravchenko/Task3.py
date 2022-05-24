# В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов. 
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import math
from decimal import Decimal
#Примечание -- я считаю, что у 5 - вещественная часть = 0
numbers_list = ["1.1", "1.2", "3.1", "5", "10.01"]
decimal_numbers_list = list(map(Decimal, numbers_list))


min_fractional = decimal_numbers_list[0] - math.floor(decimal_numbers_list[0])
max_fractional = decimal_numbers_list[0] - math.floor(decimal_numbers_list[0])

for i in range(len(numbers_list)):
    if decimal_numbers_list[i] - math.floor(decimal_numbers_list[i]) > max_fractional:
        max_fractional = decimal_numbers_list[i] - math.floor(decimal_numbers_list[i])
    
    if decimal_numbers_list[i] - math.floor(decimal_numbers_list[i]) < min_fractional:
        min_fractional = decimal_numbers_list[i] - math.floor(decimal_numbers_list[i])

print(f'Разница между максимальной вещественной частью и минимальной = {max_fractional - min_fractional}')