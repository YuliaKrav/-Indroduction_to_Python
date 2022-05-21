# Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

string_main = input("Введите основную строку: ")
string_sub = input("Введите строку-?вхождение? в основную строку: ")


part_string_main_list = string_main.split(string_sub)

print(f'Количество вхождений строки "{string_sub}" в "{string_main}" = {len(string_main.split(string_sub)) - 1}')