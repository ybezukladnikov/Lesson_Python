# 5-Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

from Main_function.Function import CheckNum

num = abs(CheckNum(int, "Input number: "))


def get_fibonachi_positiv(num: int):
    '''
    Функция возвращает одно число из ряда фибоначи.
    :param num: число, значение которого мы хотим узнать в ряде фибоначи.
    :return: число из ряда фибоначи.
    '''
    if num == 1 or num == 2:
        return 1
    else:
        return get_fibonachi_positiv(num - 1) + get_fibonachi_positiv(num - 2)


def get_fibonachi_negativ(num:int):
    '''
      Функция возвращает одно число из негативного ряда фибоначи.
      :param num: число, значение которого мы хотим узнать в негативном ряде фибоначи.
      :return: число из негативного ряда фибоначи.
    '''
    if num == 1: return 1
    if num == 2: return -1
    else:
        return get_fibonachi_negativ(num - 2) - get_fibonachi_negativ(num - 1)


def get_list_fib_neg_pos(num:int):
    '''
      Функция формирует список, объединяющий в себе два ряда
      фибоначи (позитивного и негативного)
      :param num: число, до которого мы хотим получить ряд фибаначи.
      :return: список.
    '''
    list_fib = []
    for i in range(1, num + 1):
        if i == 1: list_fib.append(0)
        list_fib.append(get_fibonachi_positiv(i))
        list_fib.insert(0, get_fibonachi_negativ(i))
    return list_fib


print(get_list_fib_neg_pos(num))
