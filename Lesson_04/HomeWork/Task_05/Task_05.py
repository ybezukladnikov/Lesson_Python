# 5 - Реализуйте RLE алгоритм: реализуйте модуль
# сжатия и восстановления данных. Входные и выходные
# данные хранятся в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# сжатый текст.


def compression():
    '''
    Функция считает повторяющиеся элементы.
    И записывает сжатую строку в файл.
    :return:
    '''
    with open('origin_text.txt', 'r') as file_obj:
        text = file_obj.read()
    compression_text = ""
    count_letter = 1
    position_sym = 0

    while position_sym<len(text)-1:
        while text[position_sym]==text[position_sym+1]:
            position_sym+=1
            count_letter+=1
            if position_sym==len(text)-1:
                break

        compression_text = compression_text + str(count_letter) + text[position_sym]
        count_letter = 1
        position_sym += 1
        if position_sym == len(text) - 1:
            compression_text = compression_text + str(count_letter) + text[position_sym]

    with open('compression_text.txt', 'w') as file_obj:
        file_obj.write(compression_text)

compression()

def recovery():
    '''
    Восстанавливает исходного строку по сжатой.
    :return:
    '''
    with open('compression_text.txt', 'r') as f:
        text = f.read()
    position_sym = 0
    recovery_text = ''

    while position_sym < len(text)-1:
        temp = ''
        while text[position_sym].isdigit():
            temp += str(text[position_sym])
            position_sym+=1
        count_letter = int(temp)

        while count_letter>0:
            recovery_text+=text[position_sym]
            count_letter-=1
        position_sym+=1
    return recovery_text


print(recovery())

