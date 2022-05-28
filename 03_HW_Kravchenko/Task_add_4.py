# 4 . Сумма квадратов первых десяти натуральных чисел равна
# 12 + 22 + ... + 102 = 385
# Квадрат суммы первых десяти натуральных чисел равен
# (1 + 2 + ... + 10)2 = 552 = 3025
# Следовательно, разность между суммой квадратов и квадратом суммы первых десяти натуральных чисел 
# составляет 3025 − 385 = 2640.
# Найдите разность между суммой квадратов и квадратом суммы первых ста натуральных чисел.

#--------------------------------------------------------------------------------------------------
#Способ 1
amount_of_numbers = 10

sum_of_squares = int((amount_of_numbers * (amount_of_numbers + 1) * (2 * amount_of_numbers + 1)) / 6)
squares_of_sum = int((amount_of_numbers * (amount_of_numbers + 1) / 2) ** 2)

print(f'Pазность между суммой квадратов и квадратом суммы первых {amount_of_numbers}'
      f' натуральных чисел с= {squares_of_sum} - {sum_of_squares} = {squares_of_sum - sum_of_squares}')


#Способ 2
sum_of_all_numbers = 0
sum_of_squares = 0
for i in range(amount_of_numbers + 1):
    sum_of_all_numbers += i
    sum_of_squares += i ** 2
 
squares_of_sum = sum_of_all_numbers ** 2

print(f'Pазность между суммой квадратов и квадратом суммы первых {amount_of_numbers}'
      f' натуральных чисел с= {squares_of_sum} - {sum_of_squares} = {squares_of_sum - sum_of_squares}')