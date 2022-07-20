'''随机出题，加减乘除'''
f=open('calcu.txt','w')


class Mix:
    '''__m（默认50）题n（默认100）以内加减乘除'''
    import random
    def __init__(self,m=50,n=100):
        self.__m=m
        self.__n=n
    def get_m(self):
        return (self.__m)
    def get_n(self):
        return (self.__n)
    def set_m(self,score):
        self.__m=score
    def set_n(self,score):
        self.__n=score

    def __str__(self):
        return f'{self.__m}题{self.__n}以内加减乘除'

    __repr__=__str__    @property
    def all(self,sign = ['+', '-', '×', '÷']):
        count = 0
        while(count<self.__m):
            num1 = self.random.randint(1,self.__n)
            num2 = self.random.randint(1, self.__n)
            num3 = self.random.randint(0, len(sign)-1)
            s = sign[num3]
            if s=='÷' and num1%num2!=0:
                continue
            elif s=='-' and num1 < num2:
                continue
            else:
                 count += 1
                 print('{0:<4d}{1:^3s}{2:<4d}  = '.format(num1, s, num2), end='\t\t')
                 print('{0:<4d}{1:^3s}{2:<4d}  = '.format(num1,s,num2),end='\t\t',file=f)
            if(not count%5):
                print('\n')
                print('\n', file=f)

    def add(self):
        self.all(sign=['+'])

    def sub(self):
        self.all(sign = ['-'])

    def mul(self):
        self.all(sign=['×'])

    def div(self):
        self.all(sign = ['÷'])

    def add_sub(self):
        self.all(sign = ['+', '-'])

    def mul_div(self):
        self.all(sign = ['×', '÷'])

