import nltk
import random
import time

words = nltk.corpus.words.words()
number = random.randint(97, 122)
working = 1
while working:
    print('猜一个a-z的小写字母. 输入quit退出。')
    start = time.time()
    running = 1
    count = 0


    def words_hint(num):
        letter = chr(num)
        word_bank = [w for w in words if letter in w]
        return word_bank[random.randint(0, len(word_bank))]


    print('该字母在%s这个词中！' % words_hint(number))
    while running:
        count += 1
        in_letter = input("请输入一个你猜的字母:")
        if in_letter == 'quit':
            working = 0
            break
        if len(in_letter) == 1 and in_letter.isalpha():
            words_hint(number)
            print('该字母也在%s这个词中！' % words_hint(number))
            if ord(in_letter) == number:
                if count == 1:
                    print('祝贺你，第一次就猜对了！')
                    running = 0
                else:
                    print("祝贺你, 你猜对了!")
                    print("结束.")
                    running = 0
            else:
                print("错！继续猜！")
        else:
            print('非单个字母！请重新输入。')

end = time.time()
time_range = end - start
print('耗时%.2f秒。' % time_range)



