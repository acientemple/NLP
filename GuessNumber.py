import random
number_range=random.choice([10,20,30,40,50,60,70,80,90,100,200,300,400,500,1000])
number=random.randint(0,number_range)
print('猜一个%d以内的整数'%number_range)
running=1
while running==1:
   guess=int(input("请输入一个你猜的整数:"))
   if guess==number:
       print("祝贺你, 你猜对了!")
       print("结束.")
       running=0
   elif guess<number:
       print("不，太小了。继续猜！")
   else:
       print("不，太大了。继续猜！")

input()
