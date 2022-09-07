# 2 - Напишите программу, которая принимает на вход число N и выдает
# набор произведений (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.
# Добавьте проверку числа N: чтобы пользователь не мог ввести буквы.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


while True:
    try:
        N = int(input("Input number: "))
        break
    except:
        print('It is not correct number. Try again.')

array = []
prod = 1
for i in range(1, N + 1):
    for k in range(1, i + 1):
        prod *= k
    array.append(prod)
    prod = 1

print(array)
