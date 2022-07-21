"""随机出题，加减乘除"""
f = open('calcu.txt', 'w')


class Mix():
    """m（默认50）题n（默认100）以内加减乘除"""
    import random
    sign = []

    def __init__(self, m=50, n=100):
        self.m = m
        self.n = n

    # def get_m(self):
    #     return self.m
    #
    # def get_n(self):
    #     return self.n
    #
    # def set_m(self, m):
    #     self.m = m
    #
    # def set_n(self, n):
    #     self.n = n

    def __str__(self):
        return f'{self.m}题{self.n}以内加减乘除'

    __repr__ = __str__

    def all(self):
        count = 0
        self.sign=['+', '-', '×', '÷']
        while count < self.m:
            num1 = self.random.randint(1, self.n)
            num2 = self.random.randint(1, self.n)
            s = self.random.choice(self.sign)
            if s == '÷' and num1 % num2 != 0:
                continue
            elif s == '-' and num1 < num2:
                continue
            else:
                count += 1
                print('{0:<4d}{1:^3s}{2:<4d}  = '.format(num1, s, num2), end='\t\t')
                print('{0:<4d}{1:^3s}{2:<4d}  = '.format(num1, s, num2), end='\t\t', file=f)
                if not count % 5:
                    print('\n')
                    print('\n', file=f)

    def add(self):
        self.sign = ['+']
        self.all()

    def sub(self):
        sign = ['-']
        self.all()

    def mul(self):
        sign = ['×']
        self.all()

    def div(self):
        sign = ['÷']
        self.all()

    def add_sub(self):
        sign = ['+', '-']
        self.all()

    def mul_div(self):
        sign = ['×', '÷']
        self.all()
