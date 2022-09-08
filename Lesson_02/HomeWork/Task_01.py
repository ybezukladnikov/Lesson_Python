# 1 - Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр. Учтите, что числа могут быть отрицательными
# Пример:
# 67.82 -> 23
# 0.56 -> 11


import Main_function as Base
# Вариант через строку.

num = Base.CheckNum(float)
result = int(''.join([i for i in str(num) \
                             if (i != "." and i != "-")]))

sum = 0
while result > 0:
    sum += result % 10
    result //= 10

print(sum)


