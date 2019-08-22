#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import os.path
from filename import file_name

def crawlsub():
        q=file_name()
        file_path="/home/baka/SentiMovie/Reviewcrawler/"+q
        if os.path.isfile(file_path):
            print("File Present")
        else:
            qu="scrapy crawl reviewcrawler -o "+q
            #print(q)   
            subprocess.Popen([qu], cwd="/home/baka/SentiMovie/Reviewcrawler", shell=True)
            return q