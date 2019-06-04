#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import nltk
import numpy as np 
import pandas as pd
 
from nltk.tokenize import word_tokenize
from nltk import pos_tag 
from nltk.util import ngrams

from nltk.stem.wordnet import WordNetLemmatizer
lemtzr=WordNetLemmatizer()

from nltk.stem.snowball import SnowballStemmer
#tokenization
def tokenize():
    text=open('/home/baka/nltk_data/corpora/movie_reviews/neg/cv002_17424.txt').read()
   # print (text)
    tokens= word_tokenize(text)
    print(tokens)
    return tokens

#ngrams
def ngram(tokens,n):
    bigram =list(ngrams(tokens,n))
    print(bigram)
    return bigram
#POS tagging
def POS_tag(tokens):
    tagged_tokens=nltk.pos_tag(tokens)
    print(tagged_tokens)
    for token,tag in tagged_tokens:
        #print (tag)
        if tag=='JJ' or tag=='RB' or tag=='RBR':
            print(token)
            print(tag)      
    #return tagged_tokens

#stemming
def stemmer(tokens):
    stemmer=SnowballStemmer("english")
    for w in tokens:
        stem=stemmer.stem(w)
        print(stem)
tokens=tokenize()          
#ngram(tokens,2)
tagged=POS_tag(tokens)
#stemmer(tagged)