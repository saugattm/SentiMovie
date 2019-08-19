#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pickle
import pandas as pd
#from nltk.tokenize import word_tokenize
with open("trainedmodel",'rb') as f:
    tf,svc=pickle.load(f)
# =============================================================================
# with open('trained_vectorizer','rb') as f:
#     vectorizer=pickle.load(f)
# =============================================================================

reviews=pd.read_csv('/home/baka/Downloads/IMDB Dataset.csv')
re=reviews[:10]
reviews=reviews[:10]
reviews=reviews.review
text=tf.transform(reviews)
print(svc.predict(text))
