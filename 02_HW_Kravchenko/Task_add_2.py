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



