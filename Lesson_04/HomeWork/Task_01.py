# 1 - Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

from Main_function.Function import CheckNum, is_num_simple

num = abs(CheckNum())


def get_list(num):
    '''
    Функция находит простые числа,
    которые являются множителем числа,
    которое получаем на вход функции.
    :param num:
    :return:
    '''
    try:
        list_result = []
        for i in range(2, num + 1):
            if num % i == 0 and is_num_simple(i): list_result.append(i)
        if len(list_result) == 0: raise Exception ("Test")

    except Exception:
        return "There is not simple numbers"
    else:
        return list_result


print(f'N = {num} -> {get_list(num)}')
