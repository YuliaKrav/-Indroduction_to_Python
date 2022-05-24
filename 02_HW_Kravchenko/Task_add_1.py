# Экстра-задачи:
# 1. Написать программу преобразования двоичного числа в десятичное.

def binary_to_decimal(number_binary):
    if len(number_binary) == 0:
        return 0
    
    number_decimal = 0
    index_max = len(number_binary) - 1
    for i in range(len(number_binary)):
        number_decimal += int(number_binary[index_max - i]) * (2 ** i)
    
    return number_decimal


number_binary = "1010"

print(f'Двоичное число {number_binary} = двоичному числу {binary_to_decimal(number_binary)}')
