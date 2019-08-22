#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pandas as pd
from filename import file_name,search_name
import ast
from review_classify import reviewclassify
from dataformatting import index
file =file_name()
   
file_address='/home/baka/SentiMovie/'+file
data=pd.read_csv(file_address)
q=search_name()
column_titles=data.columns.values.tolist()
cast_detail=ast.literal_eval(data.iat[int(index),5])
crew_detail=ast.literal_eval(data.iat[int(index),6])
type(crew_detail)

def tokenize(q):
    tokens= word_tokenize(q)
    #print(tokens)
    return tokens
tokens=tokenize(q)

def stopwordsremoval(tokens):
    stop_words=set(stopwords.words("english"))
    filtered_sentence=[words for words in tokens if words not in stop_words]
    filtered_sentence=' '.join(filtered_sentence)
    #print(filtered_sentence)
    return filtered_sentence

filtered_tokens=stopwordsremoval(tokens)

cast=['actors','actor','cast','casted']
direct=['director','directed']
screenplay=['screenplay' 'screen play','writer','written']
release=['released','came out']

def answers():
    if filtered_tokens =='reviews' or filtered_tokens=='review':
        return reviewclassify()
    if filtered_tokens in column_titles:
        lis= data.at[int(index),filtered_tokens]
        print("the lis is",lis)
        str1 = ''.join(lis)
        return str1
    elif filtered_tokens in cast:
        return cast_detail
    elif filtered_tokens in direct:
        return crew_detail['Director']
    elif filtered_tokens in screenplay:
        return crew_detail['Screenplay']
    elif filtered_tokens in release:
        return data.at[int(index),'release date']
    
