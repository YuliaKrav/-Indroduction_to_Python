# 2. Есть такая вещь - палиндром. Это когда слово читается с обеих сторон одинаково. Например, слово "шалаш". 
# Также есть числовой палиндром. Если при обратном чтении числа (124 - 421) не получается то же самое, то они складываются (124+421) и проверяются вновь. 
# Попробуйте написать функцию (или просто программу, но лучше все же функцию), находящую числовой палиндром.

def reversal_number(num):
    result = 0
    while num > 0:
        result = result * 10 + num % 10
        num //= 10
    return result


number = int(input("Введите число : "))

number_copy = number
while number_copy != reversal_number(number_copy):
    number_copy = number_copy + reversal_number(number_copy)


print(f'Полученный полиндром = {number_copy}')