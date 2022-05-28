# 1.	Найти НОК двух чисел

def search_for_the_greatest_common_divisor(num1, num2):
    num1, num2 = max(num1, num2), min(num1, num2)
    remainder = 1
    while (remainder != 0):
        remainder = num1 % num2
        num1, num2 = num2, remainder
    return num1


def search_for_the_lowest_common_multiple(num1, num2):
    return int((num1 * num2) / (search_for_the_greatest_common_divisor(num1, num2)))


number1 = 10
number2 = 15

print(f'НОК двух чисел {number1} и {number2} = {search_for_the_lowest_common_multiple(number1, number2)}')


