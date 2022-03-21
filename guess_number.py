from random import *
print('Добро пожаловать в числовую угадайку')


def is_valid(num):
    return num.isdigit()

hidden_number = randint(1, 100)
while True:
    num = input()
    if is_valid(num):
        num = int(num)
    else:
        print('А может быть все-таки введем целое число от 1 до 100?')
    if hidden_number > num:
        print('Ваше число меньше загаданного, попробуйте еще разок')
    elif hidden_number < num:
        print('Ваше число больше загаданного, попробуйте еще разок')
    elif hidden_number == num:
        print('Вы угадали, поздравляем!')
        break
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
