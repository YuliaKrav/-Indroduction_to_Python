# 1. Напишите программу, удаляющую из текста все слова содержащие "абв", которое регистронезависимо. Используйте знания с последней лекции. 
# Выполните ее в виде функции. 
# Пример: «абвгдеж рабав копыто фабв Абкн абрыволк аБволк»

def substring_delete (string_main, string_del, separator):
    result_list = string_main.split(separator)
    result_list = list(filter(lambda word: string_del.lower() not in word.lower(), result_list))
    return separator.join(result_list)

string_ex = "абвгдеж рабав копыто фабв Абкн абрыволк аБволк"
string_del = "абв"
separator = " "

print(substring_delete(string_ex, string_del, separator))

#*************************************************************************************************************************************************************

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

#*************************************************************************************************************************************************************
# 3. Вот вам текст:
# «Ну, вышел я, короче, из подъезда. В общем, короче говоря, шел я, кажется, в магазин. Ну,эээ, в общем, было лето, кажется.
# Как бы тепло. Солнечно, короче. Иду я, иду, в общем, по улице, а тут, короче, яма. Я, эээээ…. Упал в нее.
# И снова вышел, короче, из подъезда. Ясен пень, в магазин. В общем, лето на дворе, жарко, солнечно, птицы, короче, летают.
# Кстати, иду я по улице, иду, а тут, короче, яма. Ну, я в нее упал, в общем. Вышел из подъезда, короче. Лето на дворе, ясен пень.
# Птицы поют, короче, солнечно. В общем, в магазин мне надо. Что-то явно не так, короче. «Рекурсия», - подумал я.
# Ээээ...короче, в общем, пошел другой дорогой и не упал в эту… ээээ… яму. Хлеба купил».

# Отфильтруйте его, чтобы этот текст можно было нормально прочесть. Предусмотрите вариант, что мусорные слова могли быть написаны
# без использования запятых.
parasite_words = ['ну', 'короче', 'эту…', 'ту…', 'в общем', 'ясень пень',
                  'ясен пень', 'короче говоря', 'кажется', 'кстати', 'как бы']
extra_before_parasite_word = [',', ', ']
extra_after_parasite_word = [',', '…']


def read_text_from_file(file_name):
    with open(file_name, 'r', encoding='UTF-8') as file:
        text = file.read()
    return text


def delete_extra_spaces(original_string):

    result_string = original_string.strip()
    while "  " in result_string:
        result_string = result_string.replace("  ", " ")
    while "« " in result_string:
        result_string = result_string.replace("« ", "«")
    while " »" in result_string:
        result_string = result_string.replace(" »", "»")

    return result_string


def upper_case_after_period(original_text):

    sentences_list = original_text.split(".")
    for i in range(len(sentences_list)):
        first_letter_position = -1
        for j in range(len(sentences_list[i])):
            if 'а' <= sentences_list[i][j] <= 'я' or sentences_list[i][j] == 'ё':
                first_letter_position = j
                break
        if first_letter_position != -1:
            sentences_list[i] = sentences_list[i][: first_letter_position] + \
                sentences_list[i][first_letter_position].upper(
            ) + sentences_list[i][first_letter_position + 1:]

    return ".".join(sentences_list)


def form_parasite_words_list(original_string):
    ewords_list = list(filter(lambda words: words.lower().startswith(
        'ээ') or words.lower().endswith("ээ"), original_string.split()))
    words_list = []
    ewords_list = [word[: -1] if word[-1] ==
                   ',' else word for word in ewords_list]

    for word in parasite_words + ewords_list:
        word = word.lower()
        words_list.append(word)
        for pre in extra_before_parasite_word:
            words_list.append(pre + word)
            for post in extra_after_parasite_word:
                words_list.append(word + post)
                words_list.append(pre + word + post)

    # print(words_list)
    words_list = list(set(words_list))
    words_list.sort(key=len, reverse=True)
    return words_list


def delete_parasite_words(original_string):

    result_text = original_string.lower()
    delete_words_list = form_parasite_words_list(original_string)

    for del_word in delete_words_list:
        result_text = result_text.replace(del_word, "")

    # print(result_text)
    return result_text


def clean_text(text_string):

    result_string = delete_extra_spaces(text_string)
    result_string = delete_parasite_words(result_string)
    result_string = delete_extra_spaces(result_string)
    result_string = upper_case_after_period(result_string)
    return result_string


file_name = "file.txt"
text_string = read_text_from_file(file_name)
print(f'После фильтра текст из файла: \n{text_string}')

filtered_text = clean_text(text_string)
print(f'\nстал вот таким: \n{filtered_text}')

#*************************************************************************************************************************************************************