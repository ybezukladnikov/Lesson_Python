# 4- Шифр Цезаря - это способ шифрования, где каждая буква
# смещается на определенное количество символов влево или вправо.
# При расшифровке происходит обратная операция.
# К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо.
# "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл
# шифрованный текст, а также функцию, которая спрашивает ключ,
# считывает текст и дешифровывает его.
from random import randint

text = input("Enter the text you want to encrypt: ")

def encrypts(string:str):
    '''
    Функция шифрует текст.
    :param string:
    :return:
    '''
    alphabet_low = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = randint(-25, 25)
    while key == 0:
        key = randint(-25, 25)
    new_string = ''
    for ch in string:
        if ch == ' ':
            new_string+=' '
            continue
        if ch.isupper():
            new_string += alphabet_upper[alphabet_upper.find(ch) + key]
        else:
            new_string += alphabet_low[alphabet_low.find(ch) + key]

    with open('encrypts_text.txt','w') as f:
        f.write(new_string)
    return key


def decrypts(key):
    alphabet_low = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_string = ''
    with open('encrypts_text.txt','r') as f:
        string = f.read()
    for ch in string:
        if ch == ' ':
            new_string+=' '
            continue
        if ch.isupper():
            new_string += alphabet_upper[alphabet_upper.find(ch) - key]
        else:
            new_string += alphabet_low[alphabet_low.find(ch) - key]

    with open('decrypts_text.txt','w') as f:
        f.write(new_string)

key = encrypts(text)
decrypts(key)

with open('encrypts_text.txt', 'r') as f:
    encrypt_text = f.read()

with open('decrypts_text.txt', 'r') as f:
    decrypts_text = f.read()

print(f'Origin text => {text} '
      f'\nEncrypt text => {encrypt_text} '
      f'\nKey => {key}'
      f'\nDecrypt text => {decrypts_text}')

