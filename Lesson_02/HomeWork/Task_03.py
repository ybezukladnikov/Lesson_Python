# 3 - Палиндромом называется слово, которое в обе стороны читается одинаково: "шалаш", "кабак".
# А еще есть палиндром числа - смысл также в том, чтобы число в обе стороны читалось одинаково, но есть одно "но".
# Если перевернутое число не равно исходному, то они складываются и проверяются на палиндром еще раз.
# Это происходит до тех пор, пока не будет найден палиндром.
# Напишите такую программу, которая найдет палиндром введенного пользователем числа.

while True:
    try:
        N = int(input("Input number: "))
        break
    except:
        print('It is not correct number. Try again.')
temp = N
def Find_size(num):
    count = 0
    while num>0:
        num//=10
        count+=1
    return count

def Rev_number(num):
    rev_N = 0
    for i in range(Find_size(num) - 1, -1, -1):
        rev_N += (num % 10) * (10 ** i)
        num//=10
    return rev_N

count = 0
Flag = True
while Rev_number(N)!=N:
    res = N + Rev_number(N)
    N = res
    count+=1
    if count>100:
        Flag = False
        break

if Flag: print(f'Palindrome number {temp} is {res}')
else:print(f'Do not produce a palindrome number {temp}')





