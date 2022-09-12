# 5-Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

from Main_function.Function import CheckNum

num = abs(CheckNum(int, "Input number: "))

def fibonachi(num):
    if num==1 or num == 2: return 1
    else: return fibonachi(num-1) + fibonachi(num-2)

print(fibonachi(num))