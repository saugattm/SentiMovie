#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import pandas as pd
from chatpreprocessing import func
from chatpreprocessing import file_name

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', -1)

question = True
while (question):
    print("Hi, I am a simple querybot")
    print("\n")
    ques = input("Ask me questions about movies:\n")
    parsed_sent = func(ques)

    from crawlsubprocess import crawlsub

    if crawlsub(parsed_sent) != 'File Present':
        print("Please wait some time Crawling")
        time.sleep(15)

    #df = pd.read_csv("/home/baka/SentiMovie/Reviewcrawler/" + file_name)
    import dataformatting
    file=file_name(parsed_sent)
    file_address='/home/baka/SentiMovie/Reviewcrawler/'+file
    data=pd.read_csv(file_address)
    if len(data.index)>2:
        print("Which one do you mean?")
        print(data['title'])
        index=input("Select an index :")
    else:
        index=0

    dataformatting.data_form(parsed_sent,index, data, file)
    import queryprocessing

    answer = queryprocessing.answers(parsed_sent,index)
    print(answer)
   
    ans = input("Do you want to know about other movies too?(Y/N)")
    if ans.upper() != "Y":
        question = False

