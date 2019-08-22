#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from chatpreprocessing import filename

def file_name():
    parsed_sent=filename()
    #print(parsed_sent)
    file=parsed_sent['Movie']
    file=file.replace(" ","")
    file=file+".csv"
    return file
def search_name():
    parsed_sent=filename()
    file=parsed_sent['Search']
    return file