import random
import time
time_start=time.time()
number_range=random.choice([10,20,30,40,50,60,70,80,90,100,200,300,400,500,1000])
number=random.randint(0,number_range)
print('猜一个%d以内的整数'%number_range)
running=1
count=0
min=0
max=number_range
while running==1:
   guess=int(input("请输入一个你猜的整数:"))
   if guess==number:
       count+=1
       if count==1:
           print('恭喜你，第一次就猜中了！')
       else:
           print('恭喜你，猜中了！你共猜了%d次。'%count)
       running=0
   elif guess<number:
       count+=1
       if count==1:
           print("不，太小了。继续猜！")
           min=guess
       else:
           if guess<=min:
              print('嗨，好好想想，已经猜过%d，太小了！'%min)
           else:
              print("不，太小了。继续猜！")
              min = guess
   else:
       count+=1
       if count==1:
           print("不，太大了。继续猜！")
           max=guess
       else:
           if guess>=max:
              print('嗨，好好想想，已经猜过%d，太大了!'%max)
           else:
              print("不，太大了!继续猜！")
              max = guess


time_end=time.time()
time_range=time_end-time_start
print('耗时%.2f秒。'%time_range)