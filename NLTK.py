# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 18:20:24 2019

@author: Administrator
"""
# 3   Processing Raw Text

import nltk, re, pprint
from nltk import word_tokenize

#3.1
from urllib import request
url="http://www.gutenberg.org/files/2554/2554-0.txt"
response=request.urlopen(url)
raw=response.read().decode('utf8')

tokens=word_tokenize(raw)

text=nltk.Text(tokens)

# url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
# html=request.urlopen(url).read().decode('utf8')
# print(html[:60])