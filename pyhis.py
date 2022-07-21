from nltk.book import *
pyhis=''
for line in open('C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python37-32\\python.txt'):
    pyhis=pyhis+line
print(pyhis)
pyhis_words=FreqDist(pyhis)
for key in pyhis_words.keys():
    print(key),
    print(pyhis_words[key])
    
