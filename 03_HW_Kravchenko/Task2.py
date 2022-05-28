# 2.	Вычислить число PI c заданной точностью d
# Пример: при d = 0.001,  c= 3.141. 

# Try the Nilakantha series. 
# π=3+4/(2·3·4)-4/(4·5·6)+4/(6·7·8)-4/(8·9·10)+4/(10·11·12)-4/(12·13·14) ⋯
from decimal import Decimal

accuracy = 0.001

pi_current = Decimal(3)
i = 2
count_steps = 1
pi_next = pi_current + Decimal(4 / (i * (i + 1) * (i + 2)))
plus_or_minus = Decimal(1)
accuracy_current = abs(pi_current - pi_next)

while accuracy_current >= accuracy:
    count_steps += 1
    i += 2
    pi_current = pi_next
    plus_or_minus = -plus_or_minus
    pi_next = pi_current + (plus_or_minus * 4) / Decimal((i) * (i + 1) * (i + 2)) 
    accuracy_current = abs(pi_current - pi_next)

print(f'По методу Нилаканта получена PI с точностью {accuracy}  = {pi_next} за {count_steps} итераций')





