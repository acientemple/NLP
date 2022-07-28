"""随机出题，加减乘除（默认60题100以内自然数）"""
import random

__sign = []
m = 60  # 默认60题
n = 100  # 默认100以内

f = open('calculation.txt', 'w')


def __all():
    count = 0
    while count < m:
        num1 = random.randint(1, n)
        num2 = random.randint(1, n)
        s = random.choice(__sign)
        if s == '÷' and num1 % num2 != 0:
            continue
        elif s == '-' and num1 < num2:
            continue
        else:
            count += 1
            print('{0:^4d}{1:^3s}{2:^4d}  = '.format(num1, s, num2), end='\t')
            print('{0:^4d}{1:^3s}{2:^4d}  = '.format(num1, s, num2), end='\t', file=f)
            if not count % 4:
                print('\n')
                print('\n', file=f)


def add():
    global __sign
    __sign = ['+']
    __all()


def sub():
    global __sign
    __sign = ['-']
    __all()


def mul():
    global __sign
    __sign = ['×']
    __all()


def div():
    global __sign
    __sign = ['÷']
    __all()


def add_sub():
    global __sign
    __sign = ['+', '-']
    __all()


def mul_div():
    global __sign
    __sign = ['×', '÷']
    __all()


def mix():
    global __sign
    __sign = ['+', '-', '×', '÷']
    return __all()
