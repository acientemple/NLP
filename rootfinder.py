# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 21:18:04 2020

@author: Administrator

Find all words which contain the same root and make a concordance.
"""

import re

with open('Medterm.txt', 'r', encoding='utf-8') as f:
    content = f.read()

def rootfinder(root, text=content):
    matches = re.finditer(root, text)
    for i in matches:
       line = content[i.span()[0] - 80:i.span()[0] + 80]
       line = re.sub('\n', ' ', line)
       print(line)

print('''input 'quit' to quit!''')
root=''
while(True):
    root = input('Input the word you are looking for：')
    root = '%s' % root
    if root == 'quit':
        break
    else: rootfinder(root)

