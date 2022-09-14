# Данный файл содержит основные функции, которые используются в программе.


# Функция проверки ввода числа.

def CheckNum(type_date=int, massage="Input number: "):
    while True:
        try:
            num = type_date(input(massage))
            break
        except ValueError:
            print('It is not correct number. Try again.')

    return num


# Функция определения длины числа

def Find_size(num):
    count = 0
    while num > 0:
        num //= 10
        count += 1
    return count


# Функция разворота числа.

def Rev_number(num):
    count = 0
    temp = num
    while temp > 0:
        temp //= 10
        count += 1

    rev_N = 0
    for i in range(count - 1, -1, -1):
        rev_N += (num % 10) * (10 ** i)
        num //= 10
    return rev_N


def get_only_num(string):
    '''
    Функция вытаскивает из строки тольки число.
    :param string: получает на вход строку.
    :return: только цифры, которые были в строке.
    '''
    result = ''
    for i in string:
        if ord(i) > ord('/') and ord(i) < ord(':'):
            result += i
    return result


def is_num_simple(num):
    '''
    Функция проверяет, является ли число простым
    :param num: число, которое мы проверям.
    :return: True or False
    '''
    for i in range(2, num // 2 + 1):
        if num % i == 0: return False
    return True
