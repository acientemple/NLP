import nltk
import time
words=nltk.corpus.words.words()
time_start1=time.time()
word_max1=max(w.lower() for w in words)
time_end1=time.time()
time1=time_end1-time_start1

print('time1:',time1)
