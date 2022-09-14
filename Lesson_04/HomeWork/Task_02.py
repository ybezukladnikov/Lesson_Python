# 2 - Задайте последовательность чисел.
# Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# Не использовать множества.
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]
from random import randint

list_rand = [randint(3,7) for i in range(10)]
list_res = []
def get_list_unique_number(array):
    '''
    Функция получает на вход список и формирует
    из него новый список уникальных элементов.
    :param array:
    :return:
    '''
    list_res = []
    for el in array:
        if el not in list_res: list_res.append(el)
    return sorted(list_res)

print(f'{list_rand} -> {get_list_unique_number(list_rand)}')