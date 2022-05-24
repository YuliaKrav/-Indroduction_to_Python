# Подсчитать сумму цифр в вещественном числе.

# Предполагаем, что вещественное число будет введено верно
float_number = input("Введите вещественное число: ")

sum = 0
for el in float_number:
    if el != "." and el != "," and el != "-":
        sum += int(el)

print(f'Сумма цифр числа {float_number} = {sum}')