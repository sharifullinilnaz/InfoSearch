import nltk
import json
import string
import pymorphy2
import numpy as np
from scipy import spatial
from nltk.corpus import stopwords
nltk.download('stopwords')


class VectorSearch():

    def __init__(self, value):
        self.input_text = value
        self.result = self.vector_search(self.input_text)

    def vector_search(self, input_text):
        print('поиск 1')
        with open('./lemms_counts.txt', 'r', encoding='utf-8') as file:
            rows = [row.strip() for row in file]
        index = 0
        matrix = [[0] * 100 for _ in range(len(rows))]
        lemms = list()
        for row in rows:
            jsonLemms = json.loads(row.replace('\'', '\"'))
            lemm = jsonLemms["word"]
            lemms.append(lemm)
            pages = jsonLemms["inverted_array"]
            for page in pages:
                matrix[index][int(page) - 1] = 1
            index = index + 1
        matrix = np.array(matrix).transpose()
        input_text = [token for token in input_text.lower().split() if token not in stopwords.words(
            'russian') and token != " " and token.strip() not in string.punctuation]
        tokens = []
        for word in input_text:
            tokens.append(word)
        normal_form = [pymorphy2.MorphAnalyzer(lang='ru').parse(token)[0].normal_form for token in tokens]
        vector = [0] * len(lemms)
        for token in normal_form:
            if token in lemms:
                vector[lemms.index(token)] = 1
        document = dict()
        for index, doc in enumerate(matrix):
            document[index + 1] = 1 - spatial.distance.cosine(vector, doc) if max(doc) == 1 else 0.0
        res = []
        for elem in document.items():
            if elem[1] > 0 and elem[1] != 1:
                res.append(elem[0])
        print(document.items())
        return res

