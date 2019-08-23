#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import os.path
from chatpreprocessing import file_name

def crawlsub(parsed_sent):
        q=file_name(parsed_sent)
        file_path="/home/baka/SentiMovie/Reviewcrawler/"+q
        if os.path.isfile(file_path):
            message="File Present"
        else:
            qu="scrapy crawl reviewcrawler -o "+q
            #print(q)   
            subprocess.Popen([qu], cwd="/home/baka/SentiMovie/Reviewcrawler", shell=True)
            message="Crawling the data"
        return message