#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import nltk
from nltk.tokenize import word_tokenize
tokenizer=nltk.tokenize.punkt.PunktSentenceTokenizer()
text=open('/home/baka/nltk_data/corpora/movie_reviews/neg/cv002_17424.txt').read()
tokenized_sent=tokenizer.tokenize(text)
#print(tokenized_sent)
for sent in tokenized_sent:
    tokens=word_tokenize(tokenized_sent)
    print(tokens)