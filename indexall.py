#!/usr/bin/python
import re

def indexall(alp,string):
    lst=[]
    length=len(string)
    for i in range(length):
            if string[i]==alp:
                lst.append(i)
    print(lst)
def findall(str,string):
    lst=[i.span() for i in re.finditer(alp,string)]
    print(lst)
alp='a'
string="are you okay? yes, i'm ok, and you?"
indexall(alp,string)
findall(alp,string)



