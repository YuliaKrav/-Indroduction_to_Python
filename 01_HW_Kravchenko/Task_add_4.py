# 4. Напишите программу, обратную предыдущей: теперь вы загадываете число, а компьютер отгадывает.

import random

lower_range = 0
upper_range = 100

player_number = int(input(f'Загадайте число в диапазоне от {lower_range} до {upper_range} - '))

computer_number = random.randint(lower_range, upper_range)

isNotGuess = True

while (isNotGuess):
    computer_number = random.randint(lower_range, upper_range)
    print(f'Компьютер предложил число {computer_number}')
    if  computer_number < player_number:
        print("Компьютер предложил число меньше заданного")
        lower_range = computer_number
    elif computer_number > player_number:
        print("Компьютер предложил число больше заданного")
        upper_range = computer_number
    else:
        print("Компьютер угадал!")
        isNotGuess = False