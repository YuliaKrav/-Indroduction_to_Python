# Написать программу преобразования десятичного числа в двоичное

def decimal_to_binary(number_decimal):
    if number_decimal == 0:
         return "0"

    number_binary = ""
    while (number_decimal != 0):
        number_binary = str(number_decimal % 2) + number_binary
        number_decimal //= 2
    return number_binary


number_decimal = 10

print(f'Десятичное число {number_decimal} = двоичному числу {decimal_to_binary(number_decimal)}')

