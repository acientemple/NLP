# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 21:18:04 2020

@author: Administrator
"""

import re
import nltk
import os

with open('Medterm.txt', 'r', encoding='utf-8') as f:
    content = f.read()





def rootfinder(root, content):
    matches = re.finditer(root, content)
    for i in matches:
       line = content[i.span()[0] - 80:i.span()[0] + 80]
       line = re.sub('\n', ' ', line)
       print(line)
print('''input 'quit' to quit!''')
root=''
while(root!='quit'):
    root = input('Input the word you are looking for：')
    root = ' %s ' % root

    rootfinder(root,content)
#
# text=nltk.word_tokenize(content)
# text=nltk.Text(text)
# text.concordance(root)

