# 4 - Реализуйте выдачу случайного числа
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time или datetime (миллисекунды или наносекунды)
# - для задания случайности
# Учтите, что есть диапазон: от(минимальное) и до (максимальное)

import time

def Rand_in_time(min_val,max_val):
    num = time.time_ns()
    num = num % 1000000000

    while num > max_val:
        num -= (max_val - min_val) - 1
    return num


print(Rand_in_time(50,70))








