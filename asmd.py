"""随机出题，加减乘除（默认60题100以内自然数）"""
import random

__sign = []
f = open('calculation.txt', 'w')


def __all(m=60,n=100):
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


def add(m=60,n=100):
    global __sign
    __sign = ['+']
    __all(m,n)


def sub(m=60,n=100):
    global __sign
    __sign = ['-']
    __all(m,n)


def mul(m=60,n=100):
    global __sign
    __sign = ['×']
    __all(m,n)


def div(m=60,n=100):
    global __sign
    __sign = ['÷']
    __all(m,n)


def add_sub(m=60,n=100):
    global __sign
    __sign = ['+', '-']
    __all(m,n)


def mul_div(m=60,n=100):
    global __sign
    __sign = ['×', '÷']
    __all(m,n)


def mix(m=60,n=100):
    global __sign
    __sign = ['+', '-', '×', '÷']
    return __all(m,n)

# """100以内加减乘除"""
# mix()
#
# """100以内加减"""
# add_sub()
# add()
# sub()
#
# """10以内乘除"""
# mul(n=10)
# div(n=10)
# f.close()