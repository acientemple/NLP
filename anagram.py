import nltk
words=nltk.corpus.words.words(fileids='en')
def anagram(str,wordlist=words):
   return([w for w in wordlist if sorted(w)==sorted(str) and w!=str])
print(anagram('reliant'))