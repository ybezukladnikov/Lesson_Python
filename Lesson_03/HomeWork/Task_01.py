# 1- Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12



from Main_function.Function import CheckNum
from random import randint

size_list = abs(CheckNum(int, "Input size list: "))
rand_list = [randint(1,11) for i in range(size_list)]
list_number_on_odd_position = []

def get_sum(array):
    sum_num = 0
    for i in range(1,len(array),2):
        sum_num+= rand_list[i]
        list_number_on_odd_position.append(rand_list[i])
    return sum_num

result = get_sum(rand_list)
print(f'{rand_list} -> number on odd position is {list_number_on_odd_position}, Answer: {result} ')