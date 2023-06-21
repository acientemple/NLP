import re


def load_corpus(file_path):
    # 加载文本文件
    with open(file_path, 'r', encoding='utf-8') as f:
        corpus = f.read()

    # 建立语料库
    corpus = corpus.lower()
    corpus = re.sub(r'[^a-zA-Z0-9\s]', '', corpus)
    corpus = re.sub(r'\s+', ' ', corpus)
    corpus = corpus.split(' ')

    return corpus


def search_word(word, corpus):
    # 检索单词
    word = word.lower()
    matches = [i for i, w in enumerate(corpus) if w == word]

    # 检索词大写
    uppercase_matches = []
    for i, w in enumerate(corpus):
        if i in matches and w.isupper():
            uppercase_matches.append(i)

    # 检索词对齐
    aligned_matches = []
    for i in uppercase_matches:
        if i > 10 and i < len(corpus) - 11:
            context = corpus[i - 10:i + 11]
            if context[10] == word:
                aligned_matches.append(i)

    # 显示上下文
    for i in aligned_matches:
        context = ' '.join(corpus[i - 10:i + 11])
        print(context)

    return aligned_matches
