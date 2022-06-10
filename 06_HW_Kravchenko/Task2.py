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

