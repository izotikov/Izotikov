

def start():
    try:
        number = int(input())
    except ValueError:
        print('Значит ваше число шестнадцатеричное.')
        print('Введите ваше число еще раз.')
        number = input()
        systema = 16
        return number, systema
    print('Введите систему, в которой записано ваше число.')
    while True:
        try:
            systema = int(input())
            return number, systema
        except ValueError:
            print('Введите целое число.')

def calculator(number, systema):
    if systema != 16:
        x = 0
        for i in range(len(str(number))):
            x += int(str(number)[i]) * (systema ** (len(str(number)) - 1 - i))
        print(x)
    else:
        x = 0
        for i in range(len(str(number))):
            if not number[i].isdigit():
                a = ord(number[i]) - 55
            else:
                a = number[i]
            x += int(a) * (systema ** (len(str(number)) - 1 - i))
        print(x)


print('Введите ваше число, которое надо преобразовать в десятичную систему исчисления.')
number, systema = start()
calculator(number, systema)