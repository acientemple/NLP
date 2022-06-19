'''找出词表中任意两个个逆序词'''
import nltk
words=nltk.corpus.words.words()
word=['abc','cba','1234','4321','dde','ded']
def word_reverse(word):
    lst=list(word)
    lst.reverse()
    return(''.join(lst))
def word_list_reverse(wordlist=word):
    return([word_reverse(w) for w in wordlist])
print(word_list_reverse())