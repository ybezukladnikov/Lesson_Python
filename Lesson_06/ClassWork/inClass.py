# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,. приоритет операций стандартный.
# Дополнительное задание: Добавьте возможность использования скобок, меняющих приоритет операций
# *Пример:
# 2+2 => 4;
# 1+2*3 => 7;
#
# 10/2*5 => 25;
# 10 * 5 * => недостаточно числовых данных
# -5 + 5 => 0
# два + три => неправильный ввод: нужны числа
# (2+((5-3)*(16-14)))/3 => 2

def is_digit(char:str):
    return True if char.isdigit() else False

text = "2+3*4"

dict_op = {'+': lambda x, y: x + y,
           '-': lambda x, y: x - y,
           '*': lambda x, y: x * y,
           '/': lambda x, y: x / y,
           }

list_dig =[]
list_operator = []
x=''

for i in range(len(text)):
    if text[i].isdigit() : x += text[i]
    if text[i].isdigit() and  i == len(text)-1:
        list_dig.append(int(x))
    if not text[i].isdigit():
        list_operator.append(text[i])
        list_dig.append(int(x))
        x=''

while len(list_operator)!=0:

    temp_res = (dict_op[list_operator[0]])(list_dig[0],list_dig[1])
    list_operator.pop(0)
    list_dig.pop(0)
    list_dig.pop(0)
    list_dig.insert(0,temp_res)

print(list_dig)
print(list_operator)
# for i in range(len(list_operator)):
#     temp_res = (dict_op[list_operator[0]])(list_dig[0],list_dig[1])
#     list_operator.pop(0)
#     list_dig.pop(0)
#     list_dig.pop(0)
#     list_dig.insert(0,temp_res)



# print((dict_op[temp])(int(x), int(y)))






#
# print((dict_op[temp])(int(x), int(y)))


