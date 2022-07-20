# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 21:18:04 2020

@author: James@hznu.edu.cn
"""
import re
s=open('The Language of Medicine.txt')
s=s.read()

word=input('Input a word you are looking for：')
word=' %s '%word
matches=re.search(word,s)
def wordfinder(word,s):
    matches=re.search(word,s)
    start=matches.span()[0]
    end=matches.span()[1]
    line=s[start-80:start+80]
    line=re.sub('\n',' ',line)
    print(line)
    s=s[end:]
    return(s)
while matches:
          s=wordfinder(word,s)
          matches=re.search(word,s)


