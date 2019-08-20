#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd


data=pd.read_csv("/home/baka/SentiMovie/Reviewcrawler/AvengersEndgame.csv")
column_titles=["title","released_date","overview","language","cast_members","crew_members","genres","budget","revenue","runtime","reviews"]
data=data.reindex(columns=column_titles)

def cast_format():
    cast_detail={"actor_name":[],"actor_role":[]}
    castm=data['cast_members'][0]
    castm=castm.split(",")
    switch=1
    
    for cast in castm:
        if switch%2!=0:
            cast_detail['actor_name'].append(cast)
        else:
            cast_detail['actor_role'].append(cast)
        switch+=1  
        
    return cast_detail



def crew_format():
    
    crew_detail={"crew_member":[],"crew_role":[]}
    crewd=data['crew_members'][0]
    crewd=crewd.split(",")
    switch=1
    
    for crew in crewd:
        if switch%2!=0:
            crew_detail['crew_member'].append(crew)
        else:
            crew_detail['crew_role'].append(crew)
        switch+=1

    for r,c in zip(crew_detail['crew_member'],crew_detail['crew_role']):
        if c=='Director':
            print (r)
            return r

def review_format():
    review=data['reviews'][0]
    review=review.replace("A review by",'|')
    review=review+'|'
    count=0
    br_pos=[]
    rev=[]
    for r in review:
        count+=1
        if r=='|':
            br_pos.append(count)
    print(br_pos)
    #print(review[br_pos[0]:br_pos[1]])
    ran=len(br_pos)
    try:
        for i in range(0,ran):
            revi=review[br_pos[i]:br_pos[i+1]]
            rev.append(revi)
    except IndexError:
        pass
    
    return rev

reviews=review_format()
for review in reviews:
    print (review)
    print ('>>>>>>>')