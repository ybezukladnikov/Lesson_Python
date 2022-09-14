# 3 - В файле, содержащем фамилии студентов и их оценки,
# изменить на прописные буквы фамилии тех студентов,
# которые имеют средний балл более «4».
# Нужно перезаписать файл.
# Пример:
# Ангела Меркель 5
# Андрей Валетов 5
# Фредди Меркури 3
# Анастасия Пономарева 4

# Программа выдаст:

# АНГЕЛА МЕРКЕЛЬ 5
# АНДРЕЙ ВАЛЕТОВ 5
# Фредди Меркури 3
# Анастасия Пономарева 4

list_student = []
with open("main.txt","r") as file_obj:
    for line in file_obj:
        if '5' in line:
            line = line.upper()
        list_student.append(line.replace('\n',''))

with open("main.txt", "w") as file_obj:
    for line in list_student:
        file_obj.write(line + '\n')



