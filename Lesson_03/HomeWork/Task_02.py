# 2-Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import math
from Main_function.Function import CheckNum
from random import randint

size_list = abs(CheckNum(int, "Input size list: "))
rand_list = [randint(1,11) for i in range(size_list)]

def get_prod(array):
    result_list = []
    for i in range(math.ceil(len(array)/2)):
        result_list.append(rand_list[i]*rand_list[size_list-1-i])
    return result_list


print(f'{rand_list} => {get_prod(rand_list)}')