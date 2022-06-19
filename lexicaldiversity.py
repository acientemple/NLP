from nltk.book import *
textname=['text'+chr(i) for i in range(49,58)]
for text in textname:
    lengthtoken=len(locals()[text])
    lengthytype=len(set(locals()[text]))
    lexicaldiversity=lengthtoken/lengthytype
    bookname=locals()[text].name.upper()
    print("The word diversity of %s is %f"%(bookname,lexicaldiversity))