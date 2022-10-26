# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 21:18:04 2020

@author: James@hznu.edu.cn
"""
import re
import nltk

with open('nce.txt',encoding='utf8') as source:
    raw=source.read()

tokens=nltk.word_tokenize(raw)
sents=nltk.sent_tokenize(raw)
tokens=[w for w in tokens if w.isalpha()]
types=list(set(tokens)).sort()
text=nltk.Text(tokens)
fd=nltk.FreqDist(tokens)
tokens_tagged=nltk.tag.pos_tag(tokens,lang='eng',tagset='universal')




