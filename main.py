#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import pandas as pd
import removeold_search
from chatpreprocessing import func

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', -1)

question = True
while (question):
    print("Hi, I am a chatbot")
    print("\n")
    ques = input("Ask me questions about movies:\n")
    parsed_sent = func(ques)

    from crawlsubprocess import crawlsub

    if crawlsub(parsed_sent) != 'File Present':
        print("Please wait some time Crawling")
        time.sleep(15)

    #df = pd.read_csv("/home/baka/SentiMovie/Reviewcrawler/" + file_name)
    import dataformatting

    dataformatting.data_form(parsed_sent)
    import queryprocessing

    answer = queryprocessing.answers(parsed_sent)
    print(answer)
   
    ans = input("Do you want to know about other movies too?(Y/N)")
    removeold_search.rem()
    if ans.upper() != "Y":
        question = False

