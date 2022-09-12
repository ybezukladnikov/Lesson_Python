# 4- Напишите программу, которая будет преобразовывать десятичное число
# в двоичное. Подумайте, как это можно решить с помощью рекурсии.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10


from Main_function.Function import CheckNum

num = CheckNum(int, "Input number: ")
sign = ''
if num < 0: sign = '-'

def convert(num):
    if num ==1: return '1'
    elif num == 0: return '0'
    else: return convert(num//2)+str(num-(num//2)*2)

print(f'Binary of number {num} is {sign}{convert(abs(num))}')