# Задача с семинара:
# Задана натуральная степень n. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени n.
# Пример:
# - n=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 (коэф: []) или 10*x² = 0
# Уточнения:
# n - это степень икса первого элемента полинома
# при n =3 => 5*x*3 + 18*x**2 + 7*x + 19 = 0 - коэффициенты = [5,18,7,19]
# при n=2 => 2*x² + 4*x + 5 = 0(коэф: [2,4,5]) или x² + 5 = 0 (коэф: [1,0,5]) или 10*x²(коэф: [10,0,0]) = 0
# при n=10 => 56 * x*10 = 0
# коэффициенты - это числа перед элементами полинома.
# коэффициенты могут быть нулем, кроме первого
from random import randint

n = 3
list_coeff = [str(randint(0,100)) for i in range(n)]
list_coeff.insert(0,str(randint(1,100)))

stepeni =[str(i) for i in range(n+1)]
stepeni.reverse()

temp_list = []
for i in range(n+1):
    if list_coeff[i] != '0':
        temp_list.append(list_coeff[i]+'*'+'x'+'**'+stepeni[i])

if list_coeff[-1]!='0':temp_list[-1] = temp_list[-1][0:-5]
if list_coeff[-1]!='0' and list_coeff[-2]!='0':temp_list[-2] = temp_list[-2][0:-3]
if list_coeff[-1]=='0' and list_coeff[-2]!='0':temp_list[-1] = temp_list[-1][0:-3]

result = ' + '.join(temp_list) + ' = 0'
print(list_coeff)
print(stepeni)
print(result)

with open('main.txt','a') as f:
    f.write('n => ' + str(n) + ' ')
    f.write(result + ' ')
    f.write('коэф: ' + ', '.join(list_coeff))

