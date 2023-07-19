import nltk
from pdfminer.high_level import extract_text


def read_pdf(file_path):
    content = extract_text(file_path)
    return content
text=nltk.tokenize.word_tokenize(read_pdf('Food, Text and Culture in the Anglophone Caribbean.pdf'))
text=nltk.Text(text)
while(True):
    print("请输入索引关键词:")
    kwic=input()
    print(text.concordance(kwic,150,100))
    if kwic=='quit':
        break


