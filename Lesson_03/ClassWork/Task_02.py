# 1.Найти наиболее часто встречающийся элемент в массиве целых чисел.


list_arr = [3,8,5,3,1,3,7,8,8,8,9]

dict_my = {}
count = 0
for el in list_arr:
    if el in dict_my.keys():continue
    for i in range(len(list_arr)):
        if el == list_arr[i]:
            count+=1
    dict_my[el] = count
    count = 0

print(dict_my)

max = 0
num = 0
for key, values in dict_my.items():
    if values>max:
        max=values
        num=key

print(f'Число {num} встречается больше всех раз ({max})')

