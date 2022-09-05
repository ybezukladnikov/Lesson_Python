# Напишите программу, которая принимает на вход координаты точки
# (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).


while True:
    x,y = map(int,(input("Input coordinate X and Y between space: ").split()))
    if x*y==0: print('It is not correct coordinate. Try again.')
    else: break

if x>0 and y > 0: print('The point is in the first quarter')
if x<0 and y > 0: print('The point is in the second quarter')
if x<0 and y < 0: print('The point is in the third quarter')
if x>0 and y < 0: print('The point is in the fourth quarter')

