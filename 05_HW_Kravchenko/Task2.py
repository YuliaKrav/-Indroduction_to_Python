# 2. Вы когда-нибудь играли в игру "Крестики-нолики"? Попробуйте создать её, причем чтобы сыграть в нее можно было в одиночку.

import numpy as np


def fill_playing_field(fill_element, size_field):
    field = [''] * size_field

    #field = [field[i]]
    for i in range(size_field):
        field[i] = [fill_element] * size_field

    return field


def print_playing_field(field):

    print("    0   1   2")
    print("  -------------")
    for i in range(len(field)):
        print(f'{i} | ', end="")
        for j in range(len(field[0])):
            print(field[i][j] + " | ", end="")
        print("\n  -------------")


def if_all_elements_are_equal(elements_list, fill_element):
    return elements_list[0] != fill_element and elements_list.count(elements_list[0]) == len(elements_list)


def is_game_over(field, fill_element):

    for line in field:
        if if_all_elements_are_equal(line, fill_element):
            return True

    rows = list(zip(*field))
    for line in rows:
        if if_all_elements_are_equal(line, fill_element):
            return True

    diagonal_main = [field[i][i] for i in range(len(field))]
    if if_all_elements_are_equal(diagonal_main, fill_element):
        return True

    diagonal_secondary = [field[len(field) - 1 - i][i]
                          for i in range(len(field))]
    if if_all_elements_are_equal(diagonal_secondary, fill_element):
        return True

    return False


def tic_tac_toe_game():
    size_field = 3
    fill_element = ' '
    playing_field = fill_playing_field(fill_element, size_field)

    print_playing_field(playing_field)
    is_game = True
    is_X = True

    count = 0
    while(not is_game_over(playing_field, fill_element)):
        count += 1

        element = 'X' if is_X else '0'
        coordinate = list(map(int, input(
            f'Куда поставим {element}? Введите координаты поля от (0 0) до (2 2) через пробел: ').split(" ")))

        while playing_field[coordinate[0]][coordinate[1]] != fill_element:
            coordinate = list(map(int, input(
                f'В ячейке [{coordinate[0]}, {coordinate[1]}] уже есть {playing_field[coordinate[0]][coordinate[1]]}. Введите координаты поля еще раз от (0 0) до (2 2) через пробел: ').split(" ")))

        playing_field[coordinate[0]][coordinate[1]] = element
        is_X = not is_X

        print_playing_field(playing_field)

        if count == size_field ** 2:
            break

    if count == size_field ** 2:
        return f'Победителей нет'
    else:
        return f'Игрок, который ходил {element} победил.'


print(tic_tac_toe_game())
