#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from nltk.tree import Tree
from nltk import pos_tag, word_tokenize
import nltk
text= input("Enter your query:")
#text ="Who is the director of the Avengers?"
def func(text):
    tokens= word_tokenize(text)
    grammar="""
            Search: {<DT>?<JJ>*<NN>|<NNS>} 
            Movie: {<IN><NN>|<NNP>|<NNS>|<NPS>}
            Search: {<VBD>|<VBG>}
            """
    chunkParser = nltk.RegexpParser(grammar)
    tree = chunkParser.parse((pos_tag(tokens)))
    print(tree.draw())           
    parsed_sent = {}
    for i in tree:
        if type(i)==Tree:
            concat = ''
            #print(i.leaves)
            for token,pos in i.leaves():
                #print (pos)
                concat +=" "+token
                ner=(i.label(),concat)
               # print(ner)
            if ner[0] not in parsed_sent.keys():
                parsed_sent[ner[0]] = ner[1]
            else:
                parsed_sent[ner[0]] =  parsed_sent[ner[0]] + ner[1]
    print(parsed_sent)

func(text)