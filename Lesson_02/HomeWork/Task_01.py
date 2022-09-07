# 1 - Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр. Учтите, что числа могут быть отрицательными
# Пример:
# 67.82 -> 23
# 0.56 -> 11

# Вариант через строку.

while True:
    try:
        N = input("Input number: ")
        number = float(N)
        break

    except:
        print('It is not correct number. Try again.')

result = float(''.join([i for i in N if (i != "." and i != "-")]))
sum = 0
while result > 0:
    sum += result % 10
    result //= 10

print(sum)


