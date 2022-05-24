# 3.Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. Начиная с 1 и 2, 
# первые 10 элементов будут:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.

first_number = 1
second_number = 2
number_fibonacci_max = 4_000_000

sum_even_fibonacci = second_number

while second_number <= number_fibonacci_max:
    first_number, second_number = second_number, first_number + second_number; 
    if second_number % 2 == 0: 
        sum_even_fibonacci += second_number

print(f'Сумма всех четных элементов ряда Фибоначчи, которые не превышают {number_fibonacci_max} = {sum_even_fibonacci}')
