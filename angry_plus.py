"""随机出题，加减乘除，保存至calcu.txt文件"""
f = open('calcu.txt', 'w')
sign = []


class Mix():
    """m（默认50）题n（默认100）以内加减乘除"""
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
    # def set_m(self, m):
    #     self.m = m
    #
    # def set_n(self, n):
    #     self.n = n

    def __str__(self):
        return f'{self.m}题{self.n}以内加减乘除'

    __repr__ = __str__

    def __all(self):
        count = 0
        while count < self.m:
            num1 = self.random.randint(1, self.n)
            num2 = self.random.randint(1, self.n)
            num3 = self.random.randint(1, self.n)
            s = self.random.choice(sign)
            if s == '÷' and num1 % num2 != 0:
                continue
            elif s== '÷' and num1 % (num2*num3) !=0:
                continue
            elif s == '-' and num1 - num2 < 0:
                continue
            elif s == '-' and num1-num2-num3 < 0:
                continue
            else:
                count += 1
                print('{0:^4d}{1:^3s}{2:^4d}{3:^3s}{4:^4d}  = '.format(num1, s, num2 , s , num3), end='\t')
                print('{0:^4d}{1:^3s}{2:^4d}{3:^3s}{4:^4d}  = '.format(num1, s, num2 , s , num3), end='\t\t', file=f)
                if not count % 3:
                    print('\n')
                    print('\n', file=f)

    def add(self):
        global sign
        sign = ['+']
        self.__all()

    def sub(self):
        global sign
        sign = ['-']
        self.__all()

    def mul(self):
        global sign
        sign = ['×']
        self.__all()

    def div(self):
        global sign
        sign = ['÷']
        self.__all()

    def add_sub(self):
        global sign
        sign = ['+', '-']
        self.__all()

    def mul_div(self):
        global sign
        sign = ['×', '÷']
        self.__all()

    def mix(self):
        global sign
        sign = ['+', '-', '×', '÷']
        self.__all()
