#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

from dataload import reviews
 
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer

def cleaning(review):
    s=review
    s=s.lower()
    s=re.sub('<br />','',s)
    s = re.sub(r'[_"\-;%()|+&=*%.,!?:#$@\[\]/]', ' ', s)
    s = re.sub('\s\W',' ',s) 
    return s

reviews['review']=reviews['review'].apply(cleaning)

def tokenize(sentence):
    tokens= word_tokenize(sentence)
   # print(tokens)
    return tokens

reviews['review']=reviews['review'].apply(tokenize)

def stopwordsremoval(tokens):
    stop_words=set(stopwords.words("english"))
    filtered_sentence=[words for words in tokens if words not in stop_words]
    return filtered_sentence  
  
reviews['review']=reviews['review'].apply(stopwordsremoval)

def stemmer(filtered_tokens):
    stemmer=SnowballStemmer("english")
    stem=[stemmer.stem(w) for w in filtered_tokens]  
    filtered_text=' '.join(stem)
    return filtered_text  

#reviews['review']=reviews['review'].apply(stemmer)

def lemmatizer(filtered_tokens):
    lemmatizer=WordNetLemmatizer()
    lemma_words=[lemmatizer.lemmatize(w) for w in filtered_tokens]    
    filtered_text=' '.join(lemma_words)
    return filtered_text

reviews['review']=reviews['review'].apply(lemmatizer)

