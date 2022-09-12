# Данный файл содержит основные функции, которые используются в программе.


# Функция проверки ввода числа.

def CheckNum(type_date,massage):
    while True:
        try:
            num = type_date(input(massage))
            break
        except:
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
