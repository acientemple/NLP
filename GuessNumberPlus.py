import random
import time
time_start=time.time()

def guess_number():
    # Generate random number and get number range
    number_range = random.choice([10,20,30,40,50,60,70,80,90,100,200,300,400,500,1000])
    number = random.randint(0,number_range)
    print('猜一个%d以内的整数'%number_range)

    # Initialize variables
    running = True
    count = 0
    min_guess = 0
    max_guess = number_range

    # Loop until user guesses the number
    while running:
        try:
            guess = int(input("请输入一个你猜的整数: "))
            if guess == number:
                count += 1
                if count == 1:
                    print('恭喜你，第一次就猜中了！')
                else:
                    print('恭喜你，猜中了！你共猜了%d次。'%count)
                running = False
            elif guess < number:
                count += 1
                if count == 1:
                    print("不，太小了。继续猜！")
                    min_guess = guess
                else:
                    if guess <= min_guess:
                        print('嗨，好好想想，已经猜过%d，太小了！'%min_guess)
                    else:
                        print("不，太小了。继续猜！")
                        min_guess = guess
            else:
                count += 1
                if count == 1:
                    print("不，太大了。继续猜！")
                    max_guess = guess
                else:
                    if guess >= max_guess:
                        print('嗨，好好想想，已经猜过%d，太大了!'%max_guess)
                    else:
                        print("不，太大了!继续猜！")
                        max_guess = guess
        except ValueError:
            print("请输入一个整数！")

    # Print total time taken
    time_range = time.time() - time_start
    print('耗时%.2f秒。'%time_range)

guess_number()
