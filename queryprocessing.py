#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pandas as pd
from chatpreprocessing import file_name,search_name
import ast
from review_classify import reviewclassify
from dataformatting import data_form,temp_index
   

def tokenize(q):
    tokens= word_tokenize(q)
    #print(tokens)
    return tokens

def stopwordsremoval(tokens):
    stop_words=set(stopwords.words("english"))
    filtered_sentence=[words for words in tokens if words not in stop_words]
    filtered_sentence=' '.join(filtered_sentence)
    #print(filtered_sentence)
    return filtered_sentence


cast=['actors','actor','cast','casted']
direct=['director','directed']
screenplay=['screenplay' 'screen play','writer','written']
release=['released','came out']
info=['info', 'information']
revenue=['money']

def answers(parsed_sent,index):
    file =file_name(parsed_sent)
       
    file_address='/home/baka/SentiMovie/'+file
    data=pd.read_csv(file_address)
    q=search_name(parsed_sent)
    tokens = tokenize(q)
    filtered_tokens=stopwordsremoval(tokens)
    #index =data_form(parsed_sent)
    column_titles=data.columns.values.tolist()
    cast_detail=ast.literal_eval(data.iat[int(index),5])
    crew_detail=ast.literal_eval(data.iat[int(index),6])
    #type(crew_detail)
    if filtered_tokens =='reviews' or filtered_tokens=='review':
        return reviewclassify(parsed_sent,index)
    if filtered_tokens in column_titles:
        lis= data.at[int(index),filtered_tokens]
        #print("the lis is",lis)
        str1 = ''.join(lis)
        return str1
    elif filtered_tokens in info:
        return data.at[int(index),'overview']
    elif filtered_tokens in revenue:
        return data.at[int(index),'revenue']
    
    elif filtered_tokens in cast:
        return cast_detail
    elif filtered_tokens in direct:
        return crew_detail['Director']
    elif filtered_tokens in screenplay:
        return crew_detail['Screenplay']
    elif filtered_tokens in release:
        return data.at[int(index),'release date']
