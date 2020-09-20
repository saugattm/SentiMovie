#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import os.path
from chatpreprocessing import file_name

def crawlsub(parsed_sent):
        q=file_name(parsed_sent)
        print("file_name",q)
        file_path="/home/haka/old/SentiMovie/Reviewcrawler/"+q
        if os.path.isfile(file_path):
            print("file present")
            message="File Present"
        else:
            qu="scrapy crawl reviewcrawler -o "+q
            #print(q)
            subprocess.Popen([qu], cwd="/home/haka/old/SentiMovie/Reviewcrawler", shell=True)
            message="Crawling the data"
        return message

