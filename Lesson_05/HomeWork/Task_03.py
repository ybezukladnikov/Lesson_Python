# 3-Создайте два списка — один с названиями языков программирования,
# другой — с числами от 1 до длины первого.
# ['python', 'c#']
# [1,2]
# Вам нужно сделать две функции: первая из которых создаст список кортежей,
# состоящих из номера и языка, написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# Вторая — которая отфильтрует этот список следующим образом: если сумма очков
# слова имеет в делителях номер, с которым она в паре в кортеже,
# то кортеж остается, его номер заменяется на сумму очков.
# [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (102,'C#')]
# Если нет — удаляется. Суммой очков называется сложение порядковых номеров
# букв в слове. Порядковые номера смотрите в этой таблице,
# в третьем столбце: https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
# Cложите получившиеся числа и верните из функции в качестве ответа вместе с преобразованным списком


list_languages = ['python', 'c#', 'algol','alice', 'apex', 'asp', 'atlas']
list_len_lang = [i for i in range(1, len(list_languages)+1)]

def get_list_tuple(list_1, list_2):
    list_2_ch = [i.upper() for i in list_2]
    result = list(zip(list_1,list_2_ch))
    return result

def filter(list_tuple):
    new_list_len_lang = []
    new_list_languages = []
    for i in list_tuple:
        order, languages = i
        sum_bal = 0
        for j in languages:
            sum_bal+=ord(j)
        if not sum_bal%order:
            new_list_len_lang.append(sum_bal)
            new_list_languages.append(languages)
    new_list_tuple = list(zip(new_list_len_lang,new_list_languages))
    return new_list_tuple

list_tuple = get_list_tuple(list_len_lang, list_languages)
print(list_tuple)

print(filter(list_tuple))

