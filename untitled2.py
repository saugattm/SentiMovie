#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 13:34:28 2019

@author: baka
"""
from tkinter import *
from main import get_input
import time

 
def click():
    entered_text=textentry.get()
    #print(entered_text)
    textentry.delete(0,END)
    ans,multiple_file,parsed_sent=get_input(entered_text)
    from crawlsubprocess import crawlsub
    if crawlsub(parsed_sent) != 'File Present':
        #print("Please wait some time Crawling")
        ans="Please wait some time"
        time.sleep(15)
    output=Label(window, text=ans,bg="black",fg="white",font="none 12 bold")
    output.grid(row=5,column=0,columnspan=2,sticky=W)

        

window = Tk()
 
window.title("Movie review app")
window.configure(background="black")

#create label
Label(window, text="Enter you question",bg="black",fg="white",font="none 12 bold").grid(row=1,column=0,sticky=W)

#create a text entry box
textentry=Entry(window,width=20,bg="white")
textentry.grid(row=2,column=0,sticky=W)

#creating a button
Button(window,text="SUBMIT",width=6,command=click).grid(row=3,column=0,sticky=W)

window.mainloop()