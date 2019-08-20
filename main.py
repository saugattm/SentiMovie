#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from chatpreprocessing import func
from crawlsubprocess import crawlsub
#from dataformatting import dataformat
def main():
    i=1 
    ques=input("Ask me questions about movies:\n")
    while i!=0:
        func(ques)
        c=crawlsub()
        #d=dataformat(c)
        print("Data stored in",c)
        ques=input("Do you want to ask more:\n")
        if ques.lower()=='no':
            i=0
    
main()