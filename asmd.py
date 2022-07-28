"""随机出题，加减乘除"""
import random

f = open('calculation.txt', 'w')


class Mix:
    """__m（默认50）题n（默认100）以内加减乘除"""
    import random
    def __init__(self, m=60, n=100):
        self.m = m
        self.n = n

    # def get_m(self):
    #     return self.m
    #
    # def get_n(self):
    #     return self.n
    #
    # def set_m(self, score):
    #     self.m = score
    #
    # def set_n(self, score):
    #     self.n = score

    def __str__(self):
        return f'{self.m}题{self.n}以内加减乘除'

    __repr__ = __str__

    def all(self, sign=None):
        if sign is None:
            sign = ['+', '-', '×', '÷']
        count = 0
        while count < self.m:
            num1 = self.random.randint(1, self.n)
            num2 = self.random.randint(1, self.n)
            s = random.choice(sign)
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

    def add(self):
        self.all(sign=['+'])

    def sub(self):
        self.all(sign=['-'])

    def mul(self):
        self.all(sign=['×'])

    def div(self):
        self.all(sign=['÷'])

    def add_sub(self):
        self.all(sign=['+', '-'])

    def mul_div(self):
        self.all(sign=['×', '÷'])
