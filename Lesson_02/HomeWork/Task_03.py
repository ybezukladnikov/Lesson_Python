# 3 - Палиндромом называется слово, которое в обе стороны читается одинаково: "шалаш", "кабак".
# А еще есть палиндром числа - смысл также в том, чтобы число в обе стороны читалось одинаково, но есть одно "но".
# Если перевернутое число не равно исходному, то они складываются и проверяются на палиндром еще раз.
# Это происходит до тех пор, пока не будет найден палиндром.
# Напишите такую программу, которая найдет палиндром введенного пользователем числа.

from Main_function import Function as Base

n = Base.CheckNum(int)
temp = n
count = 0
Flag = True

while Base.Rev_number(n)!=n:
    res = n + Base.Rev_number(n)
    n = res
    # Ввел ограничения на количество итераций. Не все числа имеют палиндром.
    count+=1
    if count>100:
        Flag = False
        break

if Flag: print(f'Palindrome number {temp} is {res}')
else:print(f'Do not produce a palindrome number {temp}')





