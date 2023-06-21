import random

def random_generate(a, b):
    num1 = random.randint(a, b)
    num2 = random.randint(a, b)
    operator = random.choice(['+', '-', '×'])
    if operator == '+':
        answer = num1 + num2
    elif operator== '×':
        answer = num1 * num2
    else:
        answer = num1 - num2
    question = '{} {} {} = '.format(num1, operator, num2)
    return question, answer


correct = 0
mistake = 0

while True:
    print('开始答题,按q退出')
    question, answer = random_generate(0, 20)
    print('{:<15}'.format(question), end=' ')
    user_answer = input('请输入答案：')
    if user_answer=='q':
        print('\n本轮答题结束，您做对了{}道题，做错了{}道题。'.format(correct, mistake))
        break
    else:
        user_answer=int(user_answer)
    if  user_answer == answer:
        print('✔️', end=' ')
        correct += 1
    else:
        print('❌', end=' ')
        mistake += 1



print('程序结束。')

