#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pickle
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)  
pd.set_option('display.max_colwidth', -1)
from filename import file_name

def reviewclassify():
    
    with open("trainedmodel",'rb') as f:
        tf,svc=pickle.load(f)
        
        data=pd.read_csv('/home/baka/SentiMovie/'+file_name())
        review=data['review']
        
        text=tf.transform(review)
        for senti in (svc.predict(text)):
            if senti==1:
                print("positive")
            else:
                print("negative")
        return review