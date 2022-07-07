'''随机出题，加减乘除'''
import random
sign=['+','-','×','÷']

def mix(m=100,n=20):              #100题20以内加减乘除
    count = 0
    while(count<m):
        num1=random.randint(1,n)
        num2=random.randint(1,n)
        num3=random.randint(0,3)
        s=sign[num3]
        if num3==3 and num1%num2!=0:
            continue
        if num3==1 and num1 < num2:
            continue
        else:
             count += 1
             print('{0:<2}{1:^3}{2:<3} = '.format(num1,s,num2),end='     ')
        if(not count%5):
            print('\n')

def add_sub(m=100,n=20):              #100题20以内加减法
    count = 0
    while(count<m):
        num1=random.randint(1,n)
        num2=random.randint(1,n)
        num3=random.randint(0,1)
        s=sign[num3]
        if num3==1 and num1<num2:
            continue
        else:
             count += 1
             print('{0:<2}{1:^3}{2:<3} = '.format(num1,s,num2),end='     ')
        if(not count%5):
            print('\n')


def mul_div(m=100,n=20):              #100题20以内乘除法
    count = 0
    while(count<m):
        num1=random.randint(1,n)
        num2=random.randint(1,n)
        num3=random.randint(2,3)
        s=sign[num3]
        if num3==3 and num1%num2!=0:
            continue
        else:
             count += 1
             print('{0:<2}{1:^3}{2:<3} = '.format(num1,s,num2),end='     ')
        if(not count%5):
            print('\n')

def add(m=100,n=20):#100题20以内加法
    count = 0
    while (count < m):
        num1 = random.randint(1, n)
        num2 = random.randint(1, n)
        s='+'
        count += 1
        print('{0:<2}{1:^3}{1:<2} = '.format(num1,s,num2), end='     ')
        if (not count % 5):
            print('\n')


def sub(m=100,n=20):#100题20以内减法
    count = 0
    while (count < m):
        num1 = random.randint(1, n)
        num2 = random.randint(1, n)
        s='-'
        if num1 < num2:
            continue
        else:
            count += 1
            print('{0:<2}{1:^3}{1:<2} = '.format(num1,s,num2), end='     ')
        if (not count % 5):
            print('\n')


def mul(m=100,n=20):#100题20以内乘法
    count = 0
    while (count < m):
        num1 = random.randint(1, n)
        num2 = random.randint(1, n)
        s='×'
        count += 1
        print('{0:<2} × {1:<2} = '.format(num1,num2), end='     ')
        if (not count % 5):
            print('\n')


def div(m=100,n=20):              #100题20以内除法
    count = 0
    while(count<m):
        num1=random.randint(1,n)
        num2=random.randint(1,n)
        s='÷'
        if num1%num2!=0:
            continue
        else:
             count += 1
             print('{0:<2}{1:^3}{2:<3} = '.format(num1,s,num2),end='     ')
        if(not count%5):
            print('\n')