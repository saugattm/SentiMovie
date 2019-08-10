#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
#import csv

output = subprocess.Popen(["scrapy crawl reviewcrawler -o movie_desc.csv"], shell=True)

# =============================================================================
# movie_detail = {"links":[],"overview":[],"title":[]}
# with open("movie_desc.csv") as f:
#     csv_read = csv.reader(f)
#     for row in csv_read:
#         for h, v in zip(movie_detail, row):
#             #print(h,v)
#             movie_detail[h].append(v)
# 
# print(movie_detail["links"][1])
#     
# 
# =============================================================================
