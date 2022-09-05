# Задача №2. Напишите программу для. проверки истинности
# утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

flag = True

for x in range(2):
    for y in range(2):
        for z in range(2):
            if x+y+z >=1: temp=1
            else:temp=0
            if 1-temp !=(1-x)*(1-y)*(1-z):flag = False

if flag: print('Statement is true')
else: print('Statement is false')



