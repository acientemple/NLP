import time

start = time.time()
m = '11111111111111111111111111111111111'


def mul_1s(n):
    for i in range(36):
        number = int(m[:i+1])
        print('{}个1：{} * {} = {}'.format(i+1,number, number, number * number))


mul_1s(10)


def add_n(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
        print('1到{}连加得：{}'.format(i,sum))
add_n(100)
