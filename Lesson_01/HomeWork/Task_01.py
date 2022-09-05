# Задача №1. Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли
# этот день выходным.


flag = True
while flag:
    day = int(input("Input day of week: "))
    if 1 <= day <= 5:
        print('It is Work day')
        flag = False

    elif 6 <= day <= 7:
        print('It is day off')
        flag = False
    else:
        print('It is not correct number. Try again.')





