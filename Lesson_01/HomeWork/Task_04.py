# Задача №4. Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

while True:
    num_guarter = int((input("Input number of quartet (1-4): ")))
    if num_guarter > 4 or num_guarter < 1: print('It is not correct number. Try again.')
    else: break

print(num_guarter)

if num_guarter==1: print('Coordinate will be: X > 0 and Y > 0')
if num_guarter==2: print('Coordinate will be: X < 0 and Y > 0')
if num_guarter==3: print('Coordinate will be: X < 0 and Y < 0')
if num_guarter==4: print('Coordinate will be: X > 0 and Y < 0')
