# 2 - Напишите программу, которая принимает на вход число num и выдает
# набор произведений (набор - это список) чисел от 1 до num.
# Не используйте функцию math.factorial.
# Добавьте проверку числа num: чтобы пользователь не мог ввести буквы.
# Пример:
# - пусть num = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

import Main_function as Base

num = Base.CheckNum()
array = []
prod = 1
for i in range(1, num + 1):
    for k in range(1, i + 1):
        prod *= k
    array.append(prod)
    prod = 1

print(array)
