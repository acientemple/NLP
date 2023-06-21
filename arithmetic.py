import random
import math
f = open('calcu.txt', 'w')

# 随机生成指定范围内的整数
def generate_int(min_num, max_num):
    return random.randint(min_num, max_num)

# 随机生成加、减、乘、除中的一种运算符
def generate_operator():
    operator = random.choice(['+', '-', '×', '÷'])
    return operator

# 生成算式
def generate_expression():
    # 随机生成三个算子
    num1 = generate_int(1000, 9999)
    num2 = generate_int(1000, 9999)
    num3 = generate_int(1000, 9999)
    # 随机生成两个运算符
    operator1 = generate_operator()
    operator2 = generate_operator()
    # 如果是除法运算，则保证被除数和除数的最大公约数为1
    if operator2 == '÷' and math.gcd(num2, num3) != 1:
        num2, num3 = num3, num2
    # 如果是减法运算，则保证结果不为负数
    if operator1 == '-':
        if num1 < num2:
            num1, num2 = num2, num1
        if num1 - num2 < 0:
            num1, num2 = num2, num1
    # 生成算式字符串
    expression = str(num1) + ' ' + operator1 + ' ' + str(num2) + ' ' + operator2 + ' ' + str(num3)
    return expression

# 生成60道四则运算题目
expressions = []
for i in range(60):
    expressions.append(generate_expression())

# 输出题目到控制台，每行3题
for i in range(0, len(expressions), 3):
    print(expressions[i], '\t', expressions[i + 1], '\t', expressions[i + 2],file=f)

f.close()


