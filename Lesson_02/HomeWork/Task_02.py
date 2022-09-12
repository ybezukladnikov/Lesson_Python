# 2 - Напишите программу, которая принимает на вход число num и выдает
# набор произведений (набор - это список) чисел от 1 до num.
# Не используйте функцию math.factorial.
# Добавьте проверку числа num: чтобы пользователь не мог ввести буквы.
# Пример:
# - пусть num = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

from Main_function import Function as Base

num = Base.CheckNum(int)
array = []
prod = 1
for i in range(1, num + 1):
    prod *= i
    array.append(prod)


print(array)
