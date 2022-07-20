
import nltk
pyhis=''
for line in open('C:\\Users\\Lenovo\\PycharmProjects\\NLP\\text.txt'):
    pyhis=pyhis+line
print(pyhis)
pyhis_words=nltk.word_tokenize(pyhis)
pyhis_words=nltk.FreqDist(pyhis_words)
print(pyhis_words.most_common())

