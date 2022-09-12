# 1- Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12



from Main_function.Function import CheckNum
from random import randint

size_list = CheckNum(int, "Input size list: ")
sum_num =0
rand_list = [randint(1,11) for i in range(size_list)]
for i in range(1,size_list-1,2):sum_num+= rand_list[i]

print(rand_list)
print(sum_num)