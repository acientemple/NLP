import nltk
from nltk.corpus import inaugural

cfd=nltk.ConditionalFreqDist(
    (target, fileid[:4])
    for fileid in inaugural.fileids()
    for w in inaugural.words(fileid)
    for target in ['america', 'citizen']
    if w.lower().startswith(target))

from nltk.corpus import brown
cfd=nltk.ConditionalFreqDist((genre,word)
        for genre in brown.categories()
        for word in brown.words(categories=genre)
        if word.isalpha())

genre_word = [(genre, word)
              for genre in ['news', 'romance']
              for word in brown.words(categories=genre)
              if word.isalpha()]

import nltk
from urllib import request
url="http://www.gutenberg.org/files/2554/2554-0.txt"
response=request.urlopen(url)
raw=response.read().decode('utf8')
tokens=nltk.word_tokenize(raw)
text=nltk.Text(tokens)

import bs4
from bs4 import BeautifulSoup
import urllib
from urllib import request
import re

url='https://www.crummy.com/software/BeautifulSoup/bs3/documentation.zh.html'
response=request.urlopen(url)
raw=response.read().decode('utf8')
soup=BeautifulSoup(''.join(raw),'html.parser')


import xlrd
def readExcelDataByName(fileName, sheetName):
    table = None
    errorMsg = None
    try:
        data = xlrd.open_workbook(fileName)
        table = data.sheet_by_name(sheetName)
    except Exception as msg:
        errorMsg = msg
    return (table, errorMsg)

 def readExcelDataByIndex(fileName, sheetIndex):
     table = None
     errorMsg = ""
     try:
         data = xlrd.open_workbook(fileName)
         table = data.sheet_by_index(sheetIndex)
     except Exception as msg:
         errorMsg = msg
     return (table, errorMsg)


from openpyxl import workbook
wb=workbook()
ws=wb.active
wns=wb


'''随机出题，加减乘除'''
f=open('calcu.txt','w')
import random
sign=['+','-','×','÷']

def mix(m=100,n=20,s=sign[random.randint(0, 3)]):              #100题20以内加减乘除
    count = 0
    num1 = random.randint(1, n)
    num2 = random.randint(1, n)
    while(count<m):

        if s=='÷' and num1%num2!=0:
            continue
        if s=='-' and num1 < num2:
            continue
        else:
             count += 1
             print('{0:<3}{1:^3}{2:<3}  = '.format(num1,s,num2),end='\t',file=f)
             print('{0:<3}{1:^3}{2:<3}  = '.format(num1, s, num2), end='\t')
        if(not count%5):
            print('\n',file=f)
            print('\n')

def add_sub(m=100,n=20):              #100题20以内加减法
    mix(m,n,s=sign[random.randint(0, 1)])


def mul_div(m=100,n=20):              #100题20以内乘除法
    count = 0
    while(count<m):
        num1=random.randint(1,n)
        num2=random.randint(1,n)
        num3=random.randint(2,3)
        s=sign[num3]
        if num3==3 and num1%num2!=0:
            continue
        else:
             count += 1
             print('{0:<3}{1:^3}{2:<3}  = '.format(num1,s,num2),end='      ',file=f)
             print('{0:<3}{1:^3}{2:<3}  = '.format(num1, s, num2), end='      ')
        if(not count%5):
            print('\n',file=f)
            print('\n')

def add(m=100,n=20):#100题20以内加法
    count = 0
    while (count < m):
        num1 = random.randint(1, n)
        num2 = random.randint(1, n)
        s='+'
        count += 1
        print('{0:<3}{1:^3}{2:<3}  = '.format(num1,s,num2), end='      ',file=f)
        print('{0:<3}{1:^3}{2:<3}  = '.format(num1, s, num2), end='      ')
        if (not count % 5):
            print('\n',file=f)
            print('\n')


def sub(m=100,n=20):#100题20以内减法
    count = 0
    while (count < m):
        num1 = random.randint(1, n)
        num2 = random.randint(1, n)
        s='-'
        if num1 < num2:
            continue
        else:
            count += 1
            print('{0:<3}{1:^3}{2:<3}  = '.format(num1,s,num2), end='      ',file=f)
            print('{0:<3}{1:^3}{2:<3}  = '.format(num1, s, num2), end='      ')
        if (not count % 5):
            print('\n',file=f)
            print('\n')

def mul(m=100,n=10):#100题20以内乘法
    count = 0
    while (count < m):
        num1 = random.randint(1, n)
        num2 = random.randint(1, n)
        s='×'
        count += 1
        print('{0:<3}{1:^3}{2:<3}  = '.format(num1,s,num2), end='      ',file=f)
        print('{0:<3}{1:^3}{2:<3}  = '.format(num1, s, num2), end='      ')
        if (not count % 5):
            print('\n',file=f)
            print('\n')


def div(m=100,n=20):              #100题20以内除法
    count = 0
    while(count<m):
        num1=random.randint(1,n)
        num2=random.randint(1,n)
        s='÷'
        if num1%num2!=0:
            continue
        else:
             count += 1
             print('{0:<3}{1:^3}{2:<3}  = '.format(num1,s,num2),end='      ',file=f)
             print('{0:<3}{1:^3}{2:<3}  = '.format(num1, s, num2), end='      ')
        if(not count%5):
            print('\n',file=f)
            print('\n')


import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,10,0.1)
y=np.sin(x)
plt.plot(x,y)

