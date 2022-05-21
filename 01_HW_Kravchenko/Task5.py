# Написать программу получающую набор произведений чисел от 1 до N. Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]

def multiplication_n(n):
    mult = 1
    for i in range (1, n + 1):
        mult *= i
    return mult 

N = int(input("Введите число N: "))

multiplication_list = []

for i in range(1, N + 1):
    multiplication_list.append(multiplication_n(i))

print(multiplication_list)