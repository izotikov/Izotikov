from random import *


def password():
    try:
        number = int(input())
    except ValueError:
        print('Введите целое число.')
        return password()
    print('Из скольки символов должен состоять пароль?')
    try:
        lenght = int(input())
        chars = inside_pass()
        return lenght, number, chars
    except ValueError:
        print('Введите целое число.')
        return password()


def inside_pass():
    chars = ''
    print('Включать ли цифры? (0123456789) - Да/Нет')
    while True:
        answer_digits = input()
        if answer_digits.lower() == 'да':
            print('Хорошо, в вашем пароле будут цифры')
            chars += digits
            break
        elif answer_digits.lower() == 'нет':
            print('Хорошо, в вашем пароле не будет цифр')
            break
        else:
            print('Введите "да" или "нет"')
    print('Включать ли прописные буквы? (ABCDEFGHIJKLMNOPQRSTUVWXYZ) - Да/Нет')
    while True:
        answer_propis = input()
        if answer_propis.lower() == 'да':
            print('Хорошо, в вашем пароле будут прописные буквы')
            chars += uppercase_letters
            break
        elif answer_propis.lower() == 'нет':
            print('Хорошо, в вашем пароле не будет прописных букв')
            break
        else:
            print('Введите "да" или "нет"')
    print('Включать ли строчные буквы? (abcdefghijklmnopqrstuvwxyz) - Да/Нет')
    while True:
        answer_strok = input()
        if answer_strok.lower() == 'да':
            print('Хорошо, в вашем пароле будут строчные буквы')
            chars += lowercase_letters
            break
        elif answer_strok.lower() == 'нет':
            print('Хорошо, в вашем пароле не будет строчных букв')
            break
        else:
            print('Введите "да" или "нет"')
    print('Включать ли символы? (!#$%&*+-=?@^_) - Да/Нет')
    while True:
        answer_symb = input()
        if answer_symb.lower() == 'да':
            print('Хорошо, в вашем пароле будут символы')
            chars += punctuation
            break
        elif answer_symb.lower() == 'нет':
            print('Хорошо, в вашем пароле не будет символов')
            break
        else:
            print('Введите "да" или "нет"')
    return chars


def generate_password(length, number, chars):
    for j in range(number):
        your_password = ''
        for i in range(length):
            your_password += choice(chars)
        print(your_password)


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'


print('Сколько паролей вам нужно сгенерировать?')
x1, x2, x3 = password()
generate_password(x1, x2, x3)
