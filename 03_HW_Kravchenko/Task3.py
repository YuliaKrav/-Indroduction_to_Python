# 3.	Составить список простых множителей натурального числа N

def search_for_prime_multipliers(n):
    divider = 2
    multipliers_list = []

    while (divider <= n):
        while (n % divider == 0):
            multipliers_list.append(divider)
            n //= divider
        divider += 1
    return multipliers_list


N = 3572
print(f'Список простых множителей числа {N} = {search_for_prime_multipliers(N)}')

