import random
number_range=random.randint(97,122)
print('猜一个a-z的小写字母：')
running=1
while running==1:
   guess=ord(input("请输入一个你猜的字母:"))
   if guess==number_range:
       print("祝贺你, 你猜对了!")
       print("结束.")
       running=0
   else:
       print("错！继续猜！")

input()
