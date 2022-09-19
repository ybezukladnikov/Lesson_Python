# 2- Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета(или сколько вы зададите).
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет(или сколько вы зададите).
# Тот, кто берет последнюю конфету - проиграл.
# Предусмотрите последний ход, ибо там конфет остается меньше.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

def check_num_sweet(type_date=int, massage= "Input number of candies "
                                            "(The number of candies must be greater than 2): "):
    while True:
        try:
            num = type_date(input(massage))
            if num<2:
                print('Number less 2. Try again.')
                continue
            break
        except ValueError:
            print('It is not correct number. Try again.')

    return num

def check_num_max_sweet(total_can, type_date=int, massage= "Input number of max candies you can take "
                                            "(The number must be less than the total number of candies): "):
    while True:
        try:
            num = type_date(input(massage))
            if num>total_can:
                print('Number is greater than the total number of candies. Try again.')
                continue
            if num<1:
                print('The number cannot be less than 1. Try again.')
                continue
            break
        except ValueError:
            print('It is not correct number. Try again.')

    return num
num_sweet = check_num_sweet()
max_sweet = check_num_max_sweet(num_sweet)


while num_sweet > 0:
    print(f'Осталось конфет => {num_sweet}, взять можно до {max_sweet} конфет')
    num_cand_first_player = int(input("Первой игок, сколько конфет вы возьмете? "))
    num_sweet-=num_cand_first_player
    if num_sweet<=0:
        print('Поздравляем! Второй игрок, вы выиграли!')
        break
    print(f'Осталось конфет => {num_sweet}, взять можно до {max_sweet}')
    num_cand_second_player = int(input("Второй игок, сколько конфет вы возьмете? "))
    num_sweet -= num_cand_second_player
    if num_sweet <= 0:
        print('Поздравляем! Первый игрок, вы выиграли!')
        break

# print('конец')