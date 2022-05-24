#***************************************************************************************************************
# 1. Найти сумму чисел списка стоящих на нечетной позиции 

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

#***************************************************************************************************************
# 2. Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 

#numbers_list = []
numbers_list = [2, 3, 4, 5, 6]
#numbers_list = [2, 3, 5, 6]

last_i = len(numbers_list) // 2 if  len(numbers_list) % 2 == 0 else len(numbers_list) // 2 + 1
result_list = []

for i in range(last_i):
    result_list.append(numbers_list[i] * numbers_list[len(numbers_list) - 1 - i])


print(result_list)

#***************************************************************************************************************
# 3. В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов. 
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

#***************************************************************************************************************
# 4. Написать программу преобразования десятичного числа в двоичное

def decimal_to_binary(number_decimal):
    if number_decimal == 0:
         return "0"

    number_binary = ""
    while (number_decimal != 0):
        number_binary = str(number_decimal % 2) + number_binary
        number_decimal //= 2
    return number_binary


number_decimal = 10

print(f'Десятичное число {number_decimal} = двоичному числу {decimal_to_binary(number_decimal)}')

#***************************************************************************************************************
# Экстра-задачи:
# 1. Написать программу преобразования двоичного числа в десятичное.

def binary_to_decimal(number_binary):
    if len(number_binary) == 0:
        return 0
    
    number_decimal = 0
    index_max = len(number_binary) - 1
    for i in range(len(number_binary)):
        number_decimal += int(number_binary[index_max - i]) * (2 ** i)
    
    return number_decimal


number_binary = "1010"

print(f'Двоичное число {number_binary} = двоичному числу {binary_to_decimal(number_binary)}')

#***************************************************************************************************************
# Экстра-задачи:
# 2. Создайте программу, которая будет играть в игру “коровы и быки” с пользователем. Игра работает так:

# Случайным образом генерируйте 4-значное число. Попросите пользователя угадать 4-значное число. 
# За каждую цифру, которую пользователь правильно угадал в нужном месте, у них есть “корова”. 
# За каждую цифру, которую пользователь угадал правильно, в неправильном месте стоит “бык”. 
# Каждый раз, когда пользователь делает предположение, скажите им, сколько у них “коров” и “быков”. 
# Как только пользователь угадает правильное число, игра окончена. Следите за количеством догадок, 
# которые пользователь делает на протяжении всей игры, и сообщите пользователю в конце.

#Предполагается, что пользователь вводит всегда четырехзначное число
import random

def number_generation():
    possible_numbers_list = [el for el in range(10)]
    random.shuffle(possible_numbers_list)
    
    return possible_numbers_list[ : 4] if possible_numbers_list[0] != 0 else possible_numbers_list[1 : 5]

def are_unique_digits(number):
    if len(number) == len(set(number)) :
        return True
    return False

def count_bulls_and_cows(guess_number, player_number):
    count_bulls = 0
    count_cows = 0

    for i in (range(len(guess_number))):
        if guess_number[i] == player_number[i]:
            count_bulls += 1
        elif (player_number[i] in guess_number):
            count_cows += 1
    return count_bulls, count_cows

guess_number = number_generation()
#print(guess_number)

print('Игра "Быки и коровы" началась. Попробуйте угадать загаданное число.')
is_not_game_over = True
turn_of_the_game = 0
while(is_not_game_over):
    turn_of_the_game += 1
    player_number = [int(el) for el in input("Введите число (все цифры должны быть уникальными) - ")]
    if (not are_unique_digits(player_number)):
        print('В введенном вами числе есть повторяющиеся цифры. Попробуйте еще раз.')
        continue

    if guess_number != player_number:
        how_many_bools, how_many_cows = count_bulls_and_cows(guess_number, player_number)
        print(f'В введенном числе {how_many_bools} быка(ов) и {how_many_cows} коров(а)(ы)')
    else:
        is_not_game_over = False


print(f'Вы угадали число за {turn_of_the_game} хода(ов)')

#***************************************************************************************************************
# Экстра-задачи:
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

#***************************************************************************************************************
# Экстра-задачи:
# 4. Простые делители числа 13195 - это 5, 7, 13 и 29.
# Каков самый большой делитель числа 600851475143, являющийся простым числом?
import math

def is_prime(number):
    if number <= 1:
        return False
    
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    
    return True

number = 600851475143

result = ""
max_prime_divider = 0

copy_number = number

for i in range (2, number):
    if copy_number // i == 0:
        break
    if not is_prime(i):
        continue
    count_times = 0
    while (copy_number % i == 0):
        count_times += 1
        copy_number //= i

    if (count_times != 0):
        result += "(" + str(i) + " * " + str(count_times) + ")"
        max_prime_divider = i

    if (is_prime(copy_number)):
        result += "(" + str(copy_number) +  " * 1" ")" 
        max_prime_divider = copy_number
        break

print(result)
print(f'Cамый большой делитель числа {number}, являющийся простым числом - {max_prime_divider}')

#***************************************************************************************************************

