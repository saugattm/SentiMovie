#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import csv

with open('/home/baka/SentiMovie/search.csv','r') as f:
    reader=csv.reader(f)
    data=[row for row in reader]
    #print(data[1])

q = ''.join(data[1])
q=q+'.csv'
q=q.replace(" ","")
qu="scrapy crawl reviewcrawler -o "+q
print(q)

output = subprocess.Popen([qu], cwd="/home/baka/SentiMovie/Reviewcrawler", shell=True)

    

