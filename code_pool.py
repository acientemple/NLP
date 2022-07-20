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


'''exel表格操作'''
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




'''模拟进度条'''
import time
def progress(percent, symbol='█', width=80):
    if percent > 1:     # 超过 100% 的时候让其停在 1
        percent = 1     # 可以避免进度条溢出
    show_progress = ("▌%%-%ds▌" % width) % (int(percent * width) * symbol)
    print("\r%s %.2f%%" % (show_progress, percent * 100), end='')
def plan():
    data_size = 1025  # 传输数据
    recv_size = 0  # 初始值为0
    while recv_size < data_size:
        time.sleep(0.5)  # 模拟数据的传输延迟
        recv_size += 150  # 每次收150
        percent = recv_size / data_size  # 接收的比例
        progress(percent, width=80)  # 进度条的宽度40
plan()

'''模拟进度条██████████████████████████████'''
import sys,time
for i in range(30):
    sys.stdout.write("█")
    time.sleep(0.1)
    sys.stdout.flush()  # 刷新显示到屏幕

