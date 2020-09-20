#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from nltk.tree import Tree
from nltk import pos_tag, word_tokenize
import nltk
import csv

def func(text):
    parsed_sent = {}
    tokens= word_tokenize(text)
    grammar="""
            Movie: {<IN><NN>|<NNP>|<NNS>|<NPS>|<SYM>}
            Search: {<DT>?<NN>|<NNS>} 
            Search: {<VBD>|<VBG>}
            """
    chunkParser = nltk.RegexpParser(grammar)
    tree = chunkParser.parse((pos_tag(tokens)))
   # print(tree.draw())           
    for i in tree:
        if type(i)==Tree:
            concat = ''
            #print(i.leaves)
            for token,pos in i.leaves():
                #print (pos)
                concat +=" "+token
                n=(i.label(),concat)
               # print(ner)
            if n[0] not in parsed_sent.keys():
                parsed_sent[n[0]] = n[1]
            else:
                parsed_sent[n[0]] =  parsed_sent[n[0]] + n[1]
    print("the parsed_sent is:",parsed_sent)
    file_name(parsed_sent)
    search_name(parsed_sent)

    with open('search.csv','w') as f:
        writer = csv.writer(f)
        for key,val in parsed_sent.items():
            writer.writerow([val])
        f.close()
    return parsed_sent

def file_name(parsed_sent):
    #print(parsed_sent)
    file=parsed_sent['Movie']
    file=file.replace(" ","")
    file=file+".csv"
    return file
def search_name(parsed_sent):
    file=parsed_sent['Search']
    return file
text="What is the budget of Intern"
#func(text)  
