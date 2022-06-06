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
