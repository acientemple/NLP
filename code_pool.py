import nltk
from nltk.corpus import inaugural

cfd=nltk.ConditionalFreqDist(
    (target, fileid[:4])
    for fileid in inaugural.fileids()
    for w in inaugural.words(fileid)
    for target in ['america', 'citizen']
    if w.lower().startswith(target))

from nltk.corpus import brown
cfd=nltk.ConditionalFreqDist((genre,word)
        for genre in brown.categories()
        for word in brown.words(categories=genre)
        if word.isalpha())

genre_word = [(genre, word)
              for genre in ['news', 'romance']
              for word in brown.words(categories=genre)
              if word.isalpha()]

