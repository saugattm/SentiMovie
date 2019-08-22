#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import pandas as pd 
pd.set_option('display.max_columns', None)  # or 1000
pd.set_option('display.max_rows', None)  # or 1000
pd.set_option('display.max_colwidth', -1)
from chatpreprocessing import func
ques=input("Ask me questions about movies:\n")
func(ques)

import filename
file_name=filename.file_name()
print(file_name)

from crawlsubprocess import crawlsub
crawlsub()

print("Please wait some time")
time.sleep(10)


import dataformatting
dataformatting.data_form()
import queryprocessing
answer=queryprocessing.answers()
answer=[a.replace("|","________________________________________") for a in answer]


print(answer)

