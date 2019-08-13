#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

from dataload import reviews
from train_testsplit import *
 
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer

from sklearn.feature_extraction.text import TfidfVectorizer

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
    
def tfidf():
    tf=TfidfVectorizer(min_df=5,max_df=0.8,ngram_range=(1,3),use_idf=True,analyzer='word')
    tftrain_reviews=tf.fit_transform(train_reviews)
    tftest_reviews=tf.fit_transform(test_reviews)
    print(tftrain_reviews.shape)
    print(tftest_reviews.shape)
    print(tf.get_feature_names())

tfidf()
