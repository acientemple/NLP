import nltk
from nltk.corpus import inaugural

cfd = nltk.ConditionalFreqDist(
    (target, fileid[:4])
    for fileid in inaugural.fileids()
    for w in inaugural.words(fileid)
    for target in ['america', 'citizen']
    if w.lower().startswith(target))

from nltk.corpus import brown

cfd = nltk.ConditionalFreqDist((genre, word)
                               for genre in brown.categories()
                               for word in brown.words(categories=genre)
                               if word.isalpha())

genre_word = [(genre, word)
              for genre in ['news', 'romance']
              for word in brown.words(categories=genre)
              if word.isalpha()]

import nltk
from urllib import request

url = "http://www.gutenberg.org/files/2554/2554-0.txt"
response = request.urlopen(url)
raw = response.read().decode('utf8')
tokens = nltk.word_tokenize(raw)
text = nltk.Text(tokens)

import bs4
from bs4 import BeautifulSoup
import urllib
from urllib import request
import re

url = 'https://www.crummy.com/software/BeautifulSoup/bs3/documentation.zh.html'
response = request.urlopen(url)
raw = response.read().decode('utf8')
soup = BeautifulSoup(''.join(raw), 'html.parser')

import xlrd


def readExcelDataByName(fileName, sheetName):
    table = None
    errorMsg = None
    try:
        data = xlrd.open_workbook(fileName)
        table = data.sheet_by_name(sheetName)
    except Exception as msg:
        errorMsg = msg
        return table, errorMsg


def readExcelDataByIndex(fileName, sheetIndex):
    table = None
    errorMsg = ""
    try:
        data = xlrd.open_workbook(fileName)
        table = data.sheet_by_index(sheetIndex)
    except Exception as msg:
        errorMsg = msg
    return table, errorMsg


from openpyxl import workbook

wb = workbook()
ws = wb.active
wns = wb

'''随机出题，加减乘除'''
f = open('calcu.txt', 'w')
import random

sign = ['+', '-', '×', '÷']


def mix(m=100, n=20, s=sign[random.randint(0, 3)]):  # 100题20以内加减乘除
    count = 0
    num1 = random.randint(1, n)
    num2 = random.randint(1, n)
    while (count < m):

        if s == '÷' and num1 % num2 != 0:
            continue
        if s == '-' and num1 < num2:
            continue
        else:
            count += 1
            print('{0:<3}{1:^3}{2:<3}  = '.format(num1, s, num2), end='\t', file=f)
            print('{0:<3}{1:^3}{2:<3}  = '.format(num1, s, num2), end='\t')
        if (not count % 5):
            print('\n', file=f)
            print('\n')


def add_sub(m=100, n=20):  # 100题20以内加减法
    mix(m, n, s=sign[random.randint(0, 1)])


def mul_div(m=100, n=20):  # 100题20以内乘除法
    count = 0
    while (count < m):
        num1 = random.randint(1, n)
        num2 = random.randint(1, n)
        num3 = random.randint(2, 3)
        s = sign[num3]
        if num3 == 3 and num1 % num2 != 0:
            continue
        else:
            count += 1
            print('{0:<3}{1:^3}{2:<3}  = '.format(num1, s, num2), end='      ', file=f)
            print('{0:<3}{1:^3}{2:<3}  = '.format(num1, s, num2), end='      ')
        if (not count % 5):
            print('\n', file=f)
            print('\n')


def add(m=100, n=20):  # 100题20以内加法
    count = 0
    while (count < m):
        num1 = random.randint(1, n)
        num2 = random.randint(1, n)
        s = '+'
        count += 1
        print('{0:<3}{1:^3}{2:<3}  = '.format(num1, s, num2), end='      ', file=f)
        print('{0:<3}{1:^3}{2:<3}  = '.format(num1, s, num2), end='      ')
        if (not count % 5):
            print('\n', file=f)
            print('\n')


def sub(m=100, n=20):  # 100题20以内减法
    count = 0
    while (count < m):
        num1 = random.randint(1, n)
        num2 = random.randint(1, n)
        s = '-'
        if num1 < num2:
            continue
        else:
            count += 1
            print('{0:<3}{1:^3}{2:<3}  = '.format(num1, s, num2), end='      ', file=f)
            print('{0:<3}{1:^3}{2:<3}  = '.format(num1, s, num2), end='      ')
        if (not count % 5):
            print('\n', file=f)
            print('\n')


def mul(m=100, n=10):  # 100题20以内乘法
    count = 0
    while (count < m):
        num1 = random.randint(1, n)
        num2 = random.randint(1, n)
        s = '×'
        count += 1
        print('{0:<3}{1:^3}{2:<3}  = '.format(num1, s, num2), end='      ', file=f)
        print('{0:<3}{1:^3}{2:<3}  = '.format(num1, s, num2), end='      ')
        if (not count % 5):
            print('\n', file=f)
            print('\n')


def div(m=100, n=20):  # 100题20以内除法
    count = 0
    while (count < m):
        num1 = random.randint(1, n)
        num2 = random.randint(1, n)
        s = '÷'
        if num1 % num2 != 0:
            continue
        else:
            count += 1
            print('{0:<3}{1:^3}{2:<3}  = '.format(num1, s, num2), end='      ', file=f)
            print('{0:<3}{1:^3}{2:<3}  = '.format(num1, s, num2), end='      ')
        if (not count % 5):
            print('\n', file=f)
            print('\n')


import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 10, 0.1)
y = np.sin(x)
plt.plot(x, y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 100])
plt.plot(xpoints, ypoints)
plt.show()

for i in [0 - 9]:
    print(i)

for i in '0123456789abcdef':
    for j in '0123456789abcdef':
        for k in '0123456789abcdef':
            for l in '0123456789abcdef':
                print('\u{}{}{}{}'.format(i, j, k, l))

# -*- coding: UTF-8 -*-


"""判断一个unicode是否是汉字"""


def is_chinese(uchar):
    if u'\u4e00' <= uchar <= u'\u9fa5':
        return True
    else:
        return False


"""判断一个unicode是否是数字"""


def is_number(uchar):
    if u'\u0030' <= uchar <= u'\u0039':
        return True
    else:
        return False


"""判断一个unicode是否是英文字母"""


def is_alphabet(uchar):
    if (uchar >= u'\u0041' and uchar <= u'\u005a') or (uchar >= u'\u0061' and uchar <= u'\u007a'):
        return True
    else:
        return False


"""判断是否是（汉字，数字和英文字符之外的）其他字符"""


def is_other(uchar):
    if not (is_chinese(uchar) or is_number(uchar) or is_alphabet(uchar)):
        return True
    else:
        return False


"""半角转全角"""


def B2Q(uchar):
    inside_code = ord(uchar)
    if inside_code < 0x0020 or inside_code > 0x7e:  # 不是半角字符就返回原来的字符
        return uchar
    if inside_code == 0x0020:  # 除了空格其他的全角半角的公式为:半角=全角-0xfee0
        inside_code = 0x3000
    else:
        inside_code += 0xfee0
    return unichr(inside_code)


"""全角转半角"""


def Q2B(uchar):
    inside_code = ord(uchar)
    if inside_code == 0x3000:
        inside_code = 0x0020
    else:
        inside_code -= 0xfee0
    if inside_code < 0x0020 or inside_code > 0x7e:  # 转完之后不是半角字符返回原来的字符
        return uchar
    return unichr(inside_code)


"""把字符串全角转半角"""


def stringQ2B(ustring):
    return "".join([Q2B(uchar) for uchar in ustring])


"""将UTF-8编码转换为Unicode编码"""


def convert_toUnicode(string):
    ustring = string
    if not isinstance(string, unicode):
        ustring = string.decode('UTF-8')
    return ustring


if __name__ == "__main__":

    ustring1 = u'收割季节 麦浪和月光 洗着快镰刀'
    string1 = 'Sky0天地Earth1*'

    ustring1 = convert_toUnicode(ustring1)
    string1 = convert_toUnicode(string1)

    for item in string1:
        # print is_chinese(item)
        # print is_number(item)
        # print is_alphabet(item)
        print
        is_other(item)

# 递归的用法
# 给出一个无序列表, 里面嵌套list, 再嵌套list,
# 需求: 将所有list中的元素合并到一个list中

l = [10, 20, [1, 2, [4, 6, 7, [5, 6, 7, ], 6, 7, 0, 5, ], 19, 20, ], 21, 23]
result = []


def test(l):
    for x in l:
        if isinstance(x, list):
            test(x)  # 递归用法, 调用自身.
        else:
            result.append(x)


test(l)
print(result)
# [10, 20, 1, 2, 4, 6, 7, 5, 6, 7, 6, 7, 0, 5, 19, 20, 21, 23]


# 扁平化处理嵌套序列

from collections import Iterable


def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x


items = [1, 2, [11, 22, [111, 222, [1111, 2222]]]]

print(list(flatten(items)))

# 问题是要创建一个包含2000年之前创建的所有标题和2000年之后创建的所有标题的列表。
from collections import namedtuple

Book = namedtuple("Book", "author title genre year price instock")
book_1 = Book("Bob", "Harry Potter", "Fantasy", 2000, 6.00, 1000)
book_2 = Book("Martha", "Hunger Games", "Psychological", 1998, 10.00, 2000)
book_3 = Book("Sam", "The Quest", "Adventure", 2010, 8.00, 5000)
book_4 = Book("Damien", "Pokemon", "Sci-Fi", 1990, 12.00, 10000)
book_5 = Book("Voldemort", "Maze Runner", "Adventure", 2015, 10.00, 50)
book_6 = Book("Anonymous", "Horror Stories Before Bed", "Horror", 2017, 18.00, 0)
book_store_inventory = [book_1, book_2, book_3, book_4, book_5, book_6]
before_2000 = []
after_2000 = []
for book in book_store_inventory:
    if book.year <= 2000:
        before_2000.append(book.title)
    else:
        after_2000.append(book.title)

import re

re.search()
import binascii
import binhex

binascii.a2b_base64()

import sre_compile

import time

start = time.time()
m = '11111111111111111111111111111111111'


def mul_1s(n):
    for i in range(n):
        number = int(m[:i])
        print('{d} * {d} = {d}'.format(number, number, number * number))


mul_1s(9)
# end = time.time()
# t = end - start
# print('Time spent:{d}'.format(t))


for i in range(111, 999):
    if not i % (1110 - i):
        if i//100!=0 and i%100//10!=0 and i%10!=0:
            if (i//100!=i%100//10!=i%10):
                print(i)


import fileinput
for line in fileinput.input('james.txt'):
    print(line)

import pandas as pd
data=pd.read_excel('2021_1.xls')
for m in data.loc:
    for n in data.loc:
        if m['s_name']==n['s_name'] and abs(m['e_ranking']-n['e_ranking'])>=8000:
            print(m,'\n',n)

for i in range(len(d.loc[:])):
    for j in range(i,len(d.loc[:])):
        if d.loc[i]['s_name']==d.loc[j]['s_name'] and d.loc[i]['major']==d.loc[j]['major'] and abs(d.loc[i]['e_ranking']-d.loc[j]['e_ranking'])>=1000:
            print(d.loc[i],'\n',d.loc[j])



#导入相关库
import  pandas as pd
import numpy as np
import os
from pandas import DataFrame,Series
import re
df =pd.read_csv(r'E:\work\daima\python\forestfires.csv') #打开文件


import nltk
wsj = nltk.corpus.treebank.tagged_words()
cfd1=nltk.ConditionalFreqDist(wsj)
cfd2=nltk.ConditionalFreqDist([(tag,word) for (word,tag) in wsj])
bigram=nltk.bigrams(wsj)
precede=[w[0] for w in bigram if w[1][1]=='VBN']

