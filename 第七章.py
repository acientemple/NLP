# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 21:32:21 2019

@author: A
dministrator
"""

#7.1.2
from random import choice
x=choice(['Hello, world!',[1,2,3,'e','e',4]])
x.count('e')
#7.2.2
class Person:
    def set_name(self,name):
        self.name=name
        
    def get_name(self):
        return self.name
    
    def greet(self):
        print("Hello, world! I'm {}.".format(self.name))
        
#7.2.3
class Bird:
    song="Cukoo"
    def sing(self):
        print(self.song)
        
#7.2.4
class Secretive:
    def __inaccessible(self):
        print("Bet you can't see me ...")
    def accessible(self):
        print("The secret message is:")
        self.__inaccessible()
        
#7.2.5
class MemberCounter:
    members=0
    def count(self):
        MemberCounter.members+=1
        
class MemberCounter:
    members=0
    def count(self):
        self.members+=1
        
def dedupe(items):
    seen=set()
    for item in items:
        if item not in seen:
            seen.add(item)
    return(list(seen))
        

        

        