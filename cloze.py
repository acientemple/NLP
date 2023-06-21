import random

# 填空的单词数量
num_blanks = 10

# 打开文本文件
with open('text.txt', 'r') as f:
    # 读取文本
    text = f.read()
    # 将文本拆分为单词列表
    words = text.split()

    # 构建填空题
    blanks = []
    for i in range(num_blanks, len(words), num_blanks):
        # 在指定位置插入下划线
        words[i] = '__________'
        # 将空的前一个单词和后一个单词作为选项
        choices = [words[i-1], words[i+1]]
        # 从文本中随机选取两个单词作为选项
        for j in range(2):
            choice = random.choice(words)
            while choice in choices:
                choice = random.choice(words)
            choices.append(choice)
        # 随机打乱选项顺序
        random.shuffle(choices)
        # 将该填空题及其选项添加到列表中
        blanks.append((i, choices))

    # 输出填空题
    for i, choices in blanks:
        print(f"第{i/10}个空是什么？")
        for j, choice in enumerate(choices):
            print(f"{j+1}. {choice}")
text=' '.join(words)
print(text)

