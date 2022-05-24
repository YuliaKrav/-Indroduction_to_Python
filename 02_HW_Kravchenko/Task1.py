# Найти сумму чисел списка стоящих на нечетной позиции 

numbers_list = [1, 4, 6, 7, -4, 5] # нечетная позиция - четный индекс

sum = 0
for i in range(len(numbers_list)):
    if (i % 2 == 0):
        sum += numbers_list[i]

print(f'Способ1: \nСумма чисел списка {numbers_list}, стоящих на нечетной позиции = {sum}')


sum = 0
for i in range( 0, len(numbers_list), 2):
    sum += numbers_list[i]

print(f'Способ2: \nСумма чисел списка {numbers_list}, стоящих на нечетной позиции = {sum}')