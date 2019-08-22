#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import pandas as pd 
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)  
pd.set_option('display.max_colwidth', -1)
from chatpreprocessing import func
print("Hi, I am a chatbot")
print("\n")
ques=input("Ask me questions about movies:\n")
func(ques)

import filename
file_name=filename.file_name()
print(file_name)

from crawlsubprocess import crawlsub

if crawlsub()!='File Present':
    print("Please wait some time Crawling")
    time.sleep(20)

df=pd.read_csv("/home/baka/SentiMovie/Reviewcrawler/"+file_name)
import dataformatting
dataformatting.data_form()
import queryprocessing
answer=queryprocessing.answers()
#answer=[a.replace("|","________________________________________") for a in answer]
print(answer)


        
