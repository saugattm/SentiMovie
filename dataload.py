#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os 
import pandas as pd

posfiles=[x for x in os.listdir("/home/baka/SentiMovie/Data/train/pos/")]
negfiles=[x for x in os.listdir("/home/baka/SentiMovie/Data/train/neg/")]

posreviews,negreviews=[],[]


for pfile in posfiles:
    with open("/home/baka/SentiMovie/Data/train/pos/"+pfile) as f:
        posreviews.append(f.read())

for nfile in negfiles:
    with open ("/home/baka/SentiMovie/Data/train/neg/"+nfile) as f:
        negreviews.append(f.read())

reviews = pd.concat([
    pd.DataFrame({"review":posreviews, "sentiment":1, "file":posfiles}),
    pd.DataFrame({"review":negreviews, "sentiment":0, "file":negfiles}),
], ignore_index=True).sample(frac=0.5,random_state=1)
