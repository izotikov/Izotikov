from random import *

def diapason():
    try:
        n1 = int(input('В радиусе от: '))
        n2 = int(input('До: '))
    except ValueError:
        print('Одно из ваших чисел не целое, попробуйте ещё раз.')
        return diapason()
    try:
        number = randint(n1, n2)
    except ValueError:
        print('Первое число должно быть больше второго, попробуйте ещё раз!')
        return diapason()
    print('Я загадал целое число, попробуй угадать какое!')
    guess_number(number, count)
def guess_number(number, count):
    try:
        user_number = int(input())
    except ValueError:
        print('Ваше число не целое, попробуйте еще разок')
        return guess_number(number, count)
    if user_number == number:
        count += 1
        if count == 1:
            print(f'Вы угадали, поздравляем! Вам понадобилась всего {count} попытка!')
        elif 2 <= count <= 4:
            print(f'Вы угадали, поздравляем! Вам понадобилось всего {count} попытки!')
        else:
            print(f'Вы угадали, поздравляем! Вам понадобилось всего {count} попыток!')
        while True:
            print('Хотите сыграть ещё раз?')
            print('Да/Нет')
            answer = input()
            if answer.lower() == 'да':
                print('Отлично, тогда играем ещё раз!')
                return diapason()
            elif answer.lower() == 'нет':
                print('Очень жаль. До встречи!')
                break
            else:
                print('Я не понимаю, введите значения "Да" или "Нет".')
    elif user_number < number:
        count += 1
        print('Слишком мало, попробуйте еще разок')
        return guess_number(number, count)
    elif user_number > number:
        count += 1
        print('Слишком много, попробуйте еще разок')
        return guess_number(number, count)

count = 0
print('Добро пожаловать в цифровую угадайку, введите числа, в радиусе которых будем загадывать!')
diapason()


