def ngram(n,text):
    return([text[i:i+n] for i in range(len(text)-n+1)])
import nltk
text=nltk.corpus.brown.words()
print(ngram(3,text))

