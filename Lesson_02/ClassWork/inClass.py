# 1. Напишите программу, которая принимает на вход число num
# и выдаёт последовательность из num членов в виде списка
#
# *Пример:*
#
# Для num = 5: 1, -3, 9, -27, 81

# N = int(input("Input number: "))
# array =[]
#
# for i in range(0, N):
#     array.append(1*((-3)**i))
#
# print(array)


# 3.Найдите количество элементов массива, которые отличны от
# наибольшего элемента не более чем на 10% ( 10% от наибольшего)

# from random import randint
#
# array =[randint(40,100) for i in range(10)]
# num_max = max(array)
# delta = num_max/100*10
# array_1 =[]
# for el in array:
#     if el == num_max:continue
#     if el>=num_max-delta: array_1.append(el)
#
#
# print(array)
# print(num_max)
#
# print(array_1)
