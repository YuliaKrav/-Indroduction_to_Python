# 4. Простые делители числа 13195 - это 5, 7, 13 и 29.
# Каков самый большой делитель числа 600851475143, являющийся простым числом?
import math

def is_prime(number):
    if number <= 1:
        return False
    
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    
    return True

number = 600851475143

result = ""
max_prime_divider = 0

copy_number = number

for i in range (2, number):
    if copy_number // i == 0:
        break
    if not is_prime(i):
        continue
    count_times = 0
    while (copy_number % i == 0):
        count_times += 1
        copy_number //= i

    if (count_times != 0):
        result += "(" + str(i) + " * " + str(count_times) + ")"
        max_prime_divider = i

    if (is_prime(copy_number)):
        result += "(" + str(copy_number) +  " * 1" ")" 
        max_prime_divider = copy_number
        break

print(result)
print(f'Cамый большой делитель числа {number}, являющийся простым числом - {max_prime_divider}')
