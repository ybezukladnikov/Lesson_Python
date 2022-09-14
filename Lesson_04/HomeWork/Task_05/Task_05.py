# 5 - Реализуйте RLE алгоритм: реализуйте модуль
# сжатия и восстановления данных. Входные и выходные
# данные хранятся в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# сжатый текст.

#
text = "AAAAAAAAAAAA"
new_t = ""
count = 1
index = 0
flag = True
while index<len(text)-1:
    while text[index]==text[index+1]:
        index+=1
        count+=1
        if index==len(text)-1:
            break

    new_t = new_t + str(count) + text[index]
    count = 1
    index += 1
    if index == len(text) - 1:
        new_t = new_t + str(count) + text[index]

print(new_t)
############

text_1 = new_t
index = 0
res = ''
while index < len(text_1)-1:
    count = int(text_1[index])
    index+=1
    while count>0:
        res+=text_1[index]
        count-=1
    index+=1

print(res)