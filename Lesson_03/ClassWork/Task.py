# 1. Задайте список. Напишите программу, которая определит,
# присутствует ли в заданном списке строк некое число.
# ['апап4', 'fdgg3', 'fgdf', '6', 'fg24'] - ищем 24 - найдено на 4 индексе

# from Main_function.Function import CheckNum
# list_arr = ['апап4', 'fdgg3', 'fgdf', '6', 'fg24']
# num = CheckNum()
# # count = 0
# for i in range(len(list_arr)):
#     if str(num) in list_arr[i]:
#         count = i
#         break
#
# try:
#     print(count)
# except:
#     print("Такого числа нет.")


# 2. Напишите программу, которая определит позицию второго вхождения строки в
# списке либо сообщит, что её нет.
#
# *Пример:*
#
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1


# list_arr = ["qw2e", "asd", "zxc", "qwre", "ertqwe"]
# num = input("Input string: ")
# count = []
# for i in range(len(list_arr)):
#     if str(num) in list_arr[i]:
#         count.append(i)
#
# try:
#     print(count[1])
# except:
#     print("Второго вхождения в список нет.")


# 3.Для натурального n создать словарь индекс-значение,
# состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# dict_my = {}
# num = int(input("Input: "))
#
# for i in range(1, num+1):
#     dict_my[i] = 3*i+1
#
# print(dict_my)
import random

# mas = []
# list_1 = [0]*3
# for i in range(3):
#     mas.append(list_1)
#
# for i in range(len(mas)):
#     for j in range(len(mas[i])):
#         mas[i][j] = random.randint(1,10)
#         print(mas[i][j])
print("First")

mas = [[0]*2 for i in range(2)]
for i in range(len(mas)):
    for j in range(len(mas[i])):
        mas[i][j] = random.randint(1,9)
    print(mas[i])

print()
print("Second")
mas_2 = [[0]*2 for i in range(2)]
for i in range(len(mas_2)):
    for j in range(len(mas_2[i])):
        mas_2[i][j] = random.randint(1,9)
    print(mas_2[i])

print("result")
mas_3 = [[0]*2 for i in range(2)]
sum_n = 0
for i in range(len(mas_3)):
    for j in range(len(mas_3[i])):
        for k in range(len(mas_3)):
            sum_n +=mas[i][k]*mas_2[k][j]
        mas_3[i][j] = sum_n
        sum_n = 0
    print(mas_3[i])
