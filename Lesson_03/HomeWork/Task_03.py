# 3-Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением
# дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
# [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91

import math
from Main_function.Function import CheckNum
from random import random, randint

size_list = abs(CheckNum(int, "Input size list: "))
rand_list = [round((randint(1,11) + random()),randint(1,5)) for i in range(size_list)]

def get_fractional_part(num):
    return round((num - int(num)),5)

List_fractional_part = list(map(get_fractional_part,rand_list))
result = round((max(List_fractional_part)- min(List_fractional_part)),5)
another_version_result = math.ceil((result*(10**(len(str(result))-2))))

print(f'Random list = {rand_list}')
print(f'Difference between max and min = {result} or {another_version_result}')




