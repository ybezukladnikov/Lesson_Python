# Задача №2. Напишите программу для. проверки истинности
# утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# print(f'X\t\tY\t\tZ\t\tResult')
# print('*'*30)
# for x in [True, False]:
#     for y in [True, False]:
#         for z in [True, False]:
#             print(f'{x}\t{y}\t{z}\t{(not(x or y or z)) == (not x and not y and not z )} ')
from random import randint

array = [list(map(int,input("input: ").split())) for i in range(2)]
print(array)


