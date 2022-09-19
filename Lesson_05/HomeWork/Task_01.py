# 1- Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# 'абвгдейка - это передача' = >" - это передача"

text = input('Input text: ')
sub_string = input('Input sub_string: ')

list_text = text.split()
text_new =' '.join(filter(lambda x: sub_string not in x,list_text))
print(f'Initial text => {text}\nSub string => {sub_string}\nNew text => {text_new}')
