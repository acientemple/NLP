# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 20:08:54 2020

@author: Administrator
"""

def dedupe(items):
    seen=set()
    for item in items:
        if item not in seen:
            seen.add(item)
    return(list(seen))
a=(1,2,2,3,4,4)
print(dedupe(a))
list(dedupe(a))

from nltk import *
