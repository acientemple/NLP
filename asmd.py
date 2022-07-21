'''随机出题，加减乘除'''
# f=open('calcu.txt','w')


class Mix:              #100题20以内加减乘除
    import random
    sign = ['+', '-', '×', '÷']
    def __init__(self,m,n):
        self.m=m
        self.n=n

    def all(self):
        count = 0
        while(count<self.m):
            num1 = self.random.randint(1,self.n)
            num2 = self.random.randint(1, self.n)
            num3 = self.random.randint(0, len(self.sign)-1)
            s = self.sign[num3]
            if num3==3 and num1%num2!=0:
                continue
            elif num3==1 and num1 < num2:
                continue
            else:
                 count += 1
                 print('{0:<3}{1:^3}{2:<3}  = '.format(num1, s, num2), end='\t')
                 # print('{0:<3}{1:^3}{2:<3}  = '.format(num1,s,num2),end='\t',file=f)
            if(not count%5):
                print('\n')
                # print('\n', file=f)

class Add(Mix):
    sign=['+']

class Sub(Mix):
    sign = ['-']

class Mul(Mix):
    sign=['×']

class Div(Mix):
    sign = ['÷']

class Add_sub(Mix):
    sign = ['+', '-']

class Mul_div(Mix):
    sign = ['×', '÷']

