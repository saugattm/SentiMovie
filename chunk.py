#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 14:09:12 2019

@author: baka
"""
import preprocessing

def process_content():
    
    for i in tokens:
      words=nltk.word_tokenize(i)
      tagged=nltk.pos_tag(words)
      print(tagged)
      chunkGram = r"""Chunk:{<RB.?>*<VB.?>*<NNP><NN>?}"""
      chunkParser = nltk.RegexpParser(chunkGram)
      chunked = chunkParser.parse(tagged)
      chunked.draw()
process_content()

