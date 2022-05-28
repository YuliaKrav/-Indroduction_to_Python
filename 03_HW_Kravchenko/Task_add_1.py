# Экстра-задачи:
# 1.	Определите функцию, которая принимает римскую цифру в качестве аргумента и возвращает ее значение в виде 
# числового десятичного целого числа. Вам не нужно проверять форму римской цифры.
# Современные римские цифры записываются путем выражения каждой десятичной цифры числа, которое должно 
# быть закодировано отдельно, начиная с самой левой цифры. Таким образом, 1990 отображается 
# "MCMXC" (1000 = M, 900 = CM, 90 = XC), а 2008 отображается "MMVIII" (2000 = MM, 8 = VIII). 
# Римская цифра для 1666, "MDCLXVI", использует каждую букву в порядке убывания.
# Пример: имя_вашей_функции ('XXI') # должно вернуть 21

def roman_to_decimal(roman_number):
    roman_dictionary = {'M' : 1000, 'D' : 500, 'C' : 100,  'L' : 50, 'X' : 10, 'V' : 5, 'I' : 1}

    roman_number = roman_number.upper()
    roman_number_len = len(roman_number)
    decimal_number = roman_dictionary[roman_number[roman_number_len - 1]]

    for i in range(roman_number_len - 1, 0, -1):
        if roman_dictionary[roman_number[i]] > roman_dictionary[roman_number[i - 1]]:
            decimal_number -= roman_dictionary[roman_number[i - 1]]
        else:
            decimal_number += roman_dictionary[roman_number[i - 1]]
    return decimal_number

roman_number = "MXXI" # 1021
print(f'Римская цифра {roman_number} в десятичной системе = {roman_to_decimal(roman_number)}')
roman_number = "MMVIII" # 2008
print(f'Римская цифра {roman_number} в десятичной системе = {roman_to_decimal(roman_number)}')
roman_number = "MDCLXVI" # 1666
print(f'Римская цифра {roman_number} в десятичной системе = {roman_to_decimal(roman_number)}')
roman_number = "IX" # 9
print(f'Римская цифра {roman_number} в десятичной системе = {roman_to_decimal(roman_number)}')
roman_number = "CDXCVIII" # 498
print(f'Римская цифра {roman_number} в десятичной системе = {roman_to_decimal(roman_number)}')








