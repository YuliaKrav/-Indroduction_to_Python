# 1.	Найти НОК двух чисел

def search_for_the_greatest_common_divisor(num1, num2):
    num1, num2 = max(num1, num2), min(num1, num2)
    remainder = 1
    while (remainder != 0):
        remainder = num1 % num2
        num1, num2 = num2, remainder
    return num1


def search_for_the_lowest_common_multiple(num1, num2):
    return int((num1 * num2) / (search_for_the_greatest_common_divisor(num1, num2)))


number1 = 10
number2 = 15

print(f'НОК двух чисел {number1} и {number2} = {search_for_the_lowest_common_multiple(number1, number2)}')


#************************************************************************************************************

# 2.	Вычислить число PI c заданной точностью d
# Пример: при d = 0.001,  c= 3.141. 

# Try the Nilakantha series. 
# π=3+4/(2·3·4)-4/(4·5·6)+4/(6·7·8)-4/(8·9·10)+4/(10·11·12)-4/(12·13·14) ⋯
from decimal import Decimal

accuracy = 0.001

pi_current = Decimal(3)
i = 2
count_steps = 1
pi_next = pi_current + Decimal(4 / (i * (i + 1) * (i + 2)))
plus_or_minus = Decimal(1)
accuracy_current = abs(pi_current - pi_next)

while accuracy_current >= accuracy:
    count_steps += 1
    i += 2
    pi_current = pi_next
    plus_or_minus = -plus_or_minus
    pi_next = pi_current + (plus_or_minus * 4) / Decimal((i) * (i + 1) * (i + 2)) 
    accuracy_current = abs(pi_current - pi_next)

print(f'По методу Нилаканта получена PI с точностью {accuracy}  = {pi_next} за {count_steps} итераций')

#************************************************************************************************************

# 3.	Составить список простых множителей натурального числа N

def search_for_prime_multipliers(n):
    divider = 2
    multipliers_list = []

    while (divider <= n):
        while (n % divider == 0):
            multipliers_list.append(divider)
            n //= divider
        divider += 1
    return multipliers_list


N = 3572
print(f'Список простых множителей числа {N} = {search_for_prime_multipliers(N)}')

#************************************************************************************************************

# 4.	Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

numbers_list = [1, 2, 3, 5, 1, 5, 3, 10]
unique_numbers_list = set(numbers_list)

print(f'Уникальные элементы в списке {numbers_list} - {unique_numbers_list}')

#************************************************************************************************************

# 5.  Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа. 

import random

def create_int_numbers_file(file_name, amount_of_numbers, min_value, max_value, separator):
    with open(file_name, 'w') as data:
        for i in range(amount_of_numbers):
            sep = separator if i != amount_of_numbers - 1 else ""
            data.write(str(random.randint(min_value, max_value)) + sep)

def number_list_from_file(file_name, separator):
    with open(file_name, 'r') as data:
        list_numbers = list(map(int, data.read().split(separator)))
    return list_numbers

def delete_odd_numbers_from_list(list_numbers):
    return  [number for number in list_numbers if number % 2 == 0]

        
def write_odd_numbers_from_list(file_name, list_numbers, separator):
    with open(file_name, 'w') as data:
        data.write(separator.join(map(str, list_numbers)))
            
file_name = 'file.txt'
file_name_odd_numbers = 'odd_file.txt'
amount_of_numbers = 10
min_value = -7
max_value = 7
separator = " "
create_int_numbers_file(file_name, amount_of_numbers, min_value, max_value, separator)
list_numbers = number_list_from_file(file_name, separator)
list_numbers = delete_odd_numbers_from_list(list_numbers)
write_odd_numbers_from_list(file_name_odd_numbers, list_numbers, separator)


#************************************************************************************************************

# Экстра-задачи:
# 1.	Определите функцию, которая принимает римскую цифру в качестве аргумента и возвращает ее значение в виде 
# числового десятичного целого числа. Вам не нужно проверять форму римской цифры.
# Современные римские цифры записываются путем выражения каждой десятичной цифры числа, которое должно 
# быть закодировано отдельно, начиная с самой левой цифры. Таким образом, 1990 отображается 
# "MCMXC" (1000 = M, 900 = CM, 90 = XC), а 2008 отображается "MMVIII" (2000 = MM, 8 = VIII). 
# Римская цифра для 1666, "MDCLXVI", использует каждую букву в порядке убывания.
# Пример: имя_вашей_функции ('XXI') # должно вернуть 21

def roman_to_decimal(roman_number):
    roman_dictionary = {'M' : 1000, 'D' : 500, 'C' : 100,  'L' : 50, 'X' : 10, 'V' : 5, 'I' : 1}

    roman_number = roman_number.upper()
    roman_number_len = len(roman_number)
    decimal_number = roman_dictionary[roman_number[roman_number_len - 1]]

    for i in range(roman_number_len - 1, 0, -1):
        if roman_dictionary[roman_number[i]] > roman_dictionary[roman_number[i - 1]]:
            decimal_number -= roman_dictionary[roman_number[i - 1]]
        else:
            decimal_number += roman_dictionary[roman_number[i - 1]]
    return decimal_number

roman_number = "MXXI" # 1021
print(f'Римская цифра {roman_number} в десятичной системе = {roman_to_decimal(roman_number)}')
roman_number = "MMVIII" # 2008
print(f'Римская цифра {roman_number} в десятичной системе = {roman_to_decimal(roman_number)}')
roman_number = "MDCLXVI" # 1666
print(f'Римская цифра {roman_number} в десятичной системе = {roman_to_decimal(roman_number)}')
roman_number = "IX" # 9
print(f'Римская цифра {roman_number} в десятичной системе = {roman_to_decimal(roman_number)}')
roman_number = "CDXCVIII" # 498
print(f'Римская цифра {roman_number} в десятичной системе = {roman_to_decimal(roman_number)}')

# 2.	Определите функцию, которая удаляет весь текст, следующий за любым из переданных маркеров 
# комментариев. Любые пробелы в конце строки также должны быть удалены.
# Пример: 
# Входные данные:
# «apples, pears # and bananas
# grapes
# bananas !apples          » 
# Выходные данные:
# «apples, pears
# grapes
# bananas»
# Функция может вызываться вот так:
# result = function("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])

def format_string(text, markers):
    changed_text = text.rstrip()
    changed_text_list = changed_text.split("\n")
    print(changed_text_list)

    for i in range(len(changed_text_list)):
        for marker in markers:
            if marker in changed_text_list[i]: 
                changed_text_list[i] = changed_text_list[i][0 : changed_text_list[i].find(marker)]
        changed_text_list[i] = changed_text_list[i].rstrip()
    print(changed_text_list)        
    return "\n".join(changed_text_list)

original_text = "apples, pears # and bananas\ngrapes\nbananas !apples          " 
markers_list = ["#", "!"]
print(f'Если воспользоваться маркерами {markers_list}, то из текста \n{original_text}\n' 
      f'получится текст\n{format_string(original_text, markers_list)}')


#************************************************************************************************************

# 3.	Начиная в вершине треугольника (см. пример ниже) и перемещаясь вниз на смежные числа,
#  максимальная сумма до основания составляет 23.
# 4.	3
# 7 4
# 2 4 6
# 8 5 9 3
# То есть, 3 + 7 + 4 + 9 = 23.
# Найдите максимальную сумму пути от вершины до основания следующего треугольника:
# 75
# 95 64
# 17 47 82
# 18 35 87 10
# 20 04 82 47 65
# 19 01 23 75 03 34
# 88 02 77 73 07 63 67
# 99 65 04 28 06 16 70 92
# 41 41 26 56 83 40 80 70 33
# 41 48 72 33 47 32 37 16 94 29
# 53 71 44 65 25 43 91 52 97 51 14
# 70 11 33 28 77 73 17 78 39 68 17 57
# 91 71 52 38 17 14 91 43 58 50 27 29 48
# 63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

def max_value_math(triangle_list):
    row_current = len(triangle_list) - 2
    while (row_current >= 0):
        for position_in_row in range(len(triangle_list[row_current])):
            triangle_list[row_current][position_in_row] += \
            max(triangle_list[row_current + 1][position_in_row], triangle_list[row_current + 1][position_in_row +1])
        row_current -= 1 
    return triangle_list[0][0]

simple_triangle = [ 
    [3],
    [7, 4],
    [2, 4, 6],
    [8, 5, 9, 3]
]
print(f'Максимальная сумма до основания в маленьком треугольнике составляет {max_value_math(simple_triangle)}')

medium_triangle = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20,  4, 82, 47, 65],
    [19,  1, 23, 75,  3, 34],
    [88,  2, 77, 73,  7, 63, 67],
    [99, 65,  4, 28,  6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23]
]

print(f'Максимальная сумма до основания в большом треугольнике составляет {max_value_math(medium_triangle)}')

#************************************************************************************************************

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

#************************************************************************************************************

