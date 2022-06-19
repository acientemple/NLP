import nltk
from wordreverse import word_reverse,words
reversegram_list=[]
[reversegram_list.append(w) for w in words if w==word_reverse(w)]
print(reversegram_list)
input()