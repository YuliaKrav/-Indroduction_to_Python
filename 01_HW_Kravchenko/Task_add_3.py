# 3. Напишите программу, смысл которой вот в чем. Программа загадывает вам число из ограниченного диапазона. 
# Ваша цель — отгадать это за log(количество вариантов) попыток. Подсказками компьютера могут служить слова «больше» или «меньше»
import random

lower_range = 0
upper_range = 100
guess_number = random.randint(lower_range, upper_range)

isNotGuess = True

while (isNotGuess):
    player_number = int(input(f'Введите число в диапазоне от {lower_range} до {upper_range} - '))
    if player_number < guess_number:
        print("Ваше число меньше заданного")
        lower_range = player_number
    elif player_number > guess_number:
        print("Ваше число больше заданного")
        upper_range = player_number
    else:
        print("Вы угадали!")
        isNotGuess = False

