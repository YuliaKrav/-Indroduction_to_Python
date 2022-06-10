# 1 -  Написать программу вычисления арифметического выражения заданного строкой. Используются операции +,-,/,*. приоритет операций стандартный. Функцию eval не использовать!
# Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
# Дополнительно: Добавить возможность использования скобок, меняющих приоритет операций.
# Пример: 1+2*3 => 7; (1+2)*3 => 9;

import operator

opening_parenthesis = "("

expression = "2 * (3 + 1) + 2 * 2="
expression = "10 / 2 - 7 + 2 * (3 + 2 + 5 - 1) / 3 ="
OPERATORS = {'*': operator.mul, '/': operator.truediv,
             '+': operator.add, '-': operator.sub}
END_EXPRESSION = "="
OPEN_PARENTHESES = "("
CLOSE_PARENTHESES = ")"
OP_PLUS = '+'
OP_SUB = '-'
OP_MUL = '*'
OP_DIV = "/"


def delete_extra_spaces(string_original):
    return string_original.replace(" ", "")


def is_number(symbol):
    return "0" <= symbol <= "9"


def is_open_parentheses(symbol):
    return symbol == OPEN_PARENTHESES


def is_close_parentheses(symbol):
    return symbol == CLOSE_PARENTHESES


def is_math_operation(symbol):
    return symbol == OP_MUL or symbol == OP_DIV or symbol == OP_PLUS or symbol == OP_SUB


def get_number_string(expression_part_list):
    result_number_string = ""
    for i in range(len(expression_part_list)):
        if is_number(expression_part_list[i]):
            result_number_string += expression_part_list[i]
        else:
            return result_number_string


def priority_of_operation(symbol):
    if symbol == OP_MUL or symbol == OP_DIV:
        return 2
    if symbol == OP_PLUS or symbol == OP_SUB:
        return 1
    if symbol == OPEN_PARENTHESES:
        return 0


def evaluation_of_expression(expression_original):
    expression_list = list(delete_extra_spaces(expression_original))

    numbers_list = []
    operations_list = []

    def calculation_operation():
        number2 = numbers_list.pop()
        number1 = numbers_list.pop()
        return OPERATORS[operations_list.pop()](number1, number2)

    #print(OPERATORS['+']( 3, 4))
    current_position = 0
    while (expression_list[current_position] != END_EXPRESSION):
        if is_number(expression_list[current_position]):
            number_string = get_number_string(expression_list[current_position:])
            numbers_list.append(int(number_string))
            current_position += len(number_string) - 1

        elif is_open_parentheses(expression_list[current_position]):
            operations_list.append(expression_list[current_position])

        elif is_close_parentheses(expression_list[current_position]):
            while operations_list[-1] != OPEN_PARENTHESES:
                numbers_list.append(calculation_operation())
            else:
                operations_list.pop()
            
        elif is_math_operation(expression_list[current_position]):    
            current_operation = expression_list[current_position]
            current_priority = priority_of_operation(current_operation)

            while len(operations_list) > 0 and current_priority <= priority_of_operation(operations_list[-1]):
                numbers_list.append(calculation_operation())
            operations_list.append(current_operation)
        current_position += 1

    while len(operations_list) > 0:
        numbers_list.append(calculation_operation())

    return numbers_list[0]



print(f'{expression} {evaluation_of_expression(expression)}')

# **************************************************************************************************************************************************

# 2 - Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных файлах (в одном файлике отрывок 
# из какой-то книги, а втором файлике — сжатая версия этого текста). 

unique_sign = "-"

def read_from_file(file_name):
    with open(file_name, 'r', encoding = 'UTF-8') as file:
        data = file.read()
    return data

def write_to_file(file_name, data):
    with open(file_name, 'w', encoding = 'UTF-8') as file:
        file.write(data)


def is_number(symbol):
    return "0" <= symbol <= "9"

def data_compression_RLE(data):
    '''
    Функция сжатия. Если в строке несколько уникальных символов подряд, то считается их общее количество и выводится со знаком -,
    например, фываппппп = -4фыва5п
    '''

    previous_symbol = ""
    result_string = ""
    unique_symbols =""
    count = 1

    for symbol in data:
        unique_symbols += symbol 

        if previous_symbol == "":
            previous_symbol = symbol
            continue

        if previous_symbol == symbol:
            if len(unique_symbols) > 2:
                result_string += unique_sign + str(len(unique_symbols[ : -2])) + unique_symbols[ : -2]
            count += 1
            unique_symbols = ""

        else:
            if count > 1:
                result_string += str(count) + previous_symbol
                count = 1
        previous_symbol = symbol
    
    if unique_symbols != "": 
        result_string += unique_sign + str(len(unique_symbols[ : ])) + unique_symbols[ : ]
    elif count > 1:
        result_string += str(count) + previous_symbol

    return result_string


def data_uncompression_RLE(data):
    repetitions_string = ""
    result_string = ""
    index = 0

    while index < len(data):
        
        if repetitions_string == "" and data[index] == unique_sign:
            repetitions_string += data[index]
            index += 1
            continue
        
        if is_number(data[index]):
            repetitions_string += data[index]
            index += 1
            continue
   
        if int(repetitions_string) > 0:
            result_string += int(repetitions_string) * data[index] 
            index += 1
        else:
            result_string += "".join([data[index : index + abs(int(repetitions_string))]])
            index += abs(int(repetitions_string))
   
        # print(result_string)
        repetitions_string = ""
    
    return result_string

file_name = "file_before_RLE.txt"

text = read_from_file(file_name)
print(f'Original text: \n {text}')


file_name = "file_after_RLE.txt"

text_compressed = data_compression_RLE(text)
write_to_file(file_name, text_compressed)
print(f'Compressed text: \n {text_compressed}')


text_uncompressed = data_uncompression_RLE(text_compressed)
print(f'Uncompressed text: \n {text_uncompressed}')

# print(text == text_uncompressed)

# **************************************************************************************************************************************************

# 3 -  ROT13 - это простой шифр подстановки букв, который заменяет букву буквой, которая идет через 13 букв после нее в алфавите. ROT13 является примером шифра Цезаря.
# Создайте функцию, которая принимает строку и возвращает строку, зашифрованную с помощью  . Если в строку включены числа или специальные символы, они должны быть
# возвращены как есть. Также создайте функцию, которая расшифровывает эту строку обратно (некий начальный аналог шифрования сообщений).
# Не использовать функцию encode.


def read_from_file(file_name):
    with open(file_name, 'r', encoding='UTF-8') as file:
        data = file.read()
    return data


def write_to_file(file_name, data):
    with open(file_name, 'w', encoding='UTF-8') as file:
        file.write(data)


def encryption_symbol_ROT13(symbol):
    offset = 13
    new_symbol = symbol
    if symbol.isalpha():
        first_letter, last_letter = (
            "A", "Z") if symbol.isupper() else ("a", "z")
        new_symbol = chr(ord(symbol) + offset) if ord(symbol) + offset <= ord(
            last_letter) else chr(ord(first_letter) + ord(symbol) + offset - ord(last_letter) - 1)
        # alphabet_length = (ord(last_letter) - ord(first_letter) + 1)
        # symbol_code = ord(symbol) - ord(first_letter) + 1
        # new_symbol = chr((symbol_code + offset) % alphabet_length + ord(first_letter) - 1)
    return new_symbol


def encription_text(text_original):
    text_result = ""
    for symbol in text_original:
        text_result += encryption_symbol_ROT13(symbol)
    return text_result


def decryption_symbol_ROT13(symbol):
    offset = 13
    new_symbol = symbol
    if symbol.isalpha():
        first_letter, last_letter = (
            "A", "Z") if symbol.isupper() else ("a", "z")
        new_symbol = chr(ord(symbol) - offset) if ord(symbol) - offset >= ord(
            first_letter) else chr(ord(last_letter) - (ord(first_letter) - (ord(symbol) - offset) - 1))
    return new_symbol


def decription_text(text_original):
    text_result = ""
    for symbol in text_original:
        text_result += decryption_symbol_ROT13(symbol)
    return text_result


file_name = "file_before_ROT13.txt"

text = read_from_file(file_name)
print(f'Original text:\n {text}\n')

file_name = "file_after_ROT13.txt"
text_after_encryption = encription_text(text)
print(f'Text after encryption:\n {text_after_encryption}\n')
write_to_file(file_name, text_after_encryption)

text_after_decryption = decription_text(text_after_encryption)
print(f'Text after decryption:\n {text_after_decryption}')

# print(text == text_after_decryption)

# **************************************************************************************************************************************************
# **************************************************************************************************************************************************
# **************************************************************************************************************************************************