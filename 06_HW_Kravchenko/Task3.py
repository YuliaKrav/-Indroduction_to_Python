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

# for i in range(ord('A'), ord('Z') + 1):
#     print(i, chr(i))

# for i in range(ord('a'), ord('z') + 1):
#     print(i, chr(i))
# encryption_symbol_ROT13("G")
# decryption_symbol_ROT13("T")
# encryption_symbol_ROT13("h")
# decryption_symbol_ROT13("u")

# encryption_symbol_ROT13("a")
# decryption_symbol_ROT13("n")
# encryption_symbol_ROT13("z")
# decryption_symbol_ROT13("m")
# encryption_symbol_ROT13("Z")
# decryption_symbol_ROT13("M")


# encryption_symbol_ROT13("p")
# decryption_symbol_ROT13("c")
# encryption_symbol_ROT13("P")
# decryption_symbol_ROT13("C")


# encryption_symbol_ROT13(",")
# decryption_symbol_ROT13(",")
# encryption_symbol_ROT13(".")
# decryption_symbol_ROT13(".")
