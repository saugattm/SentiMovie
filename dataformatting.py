#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
from filename import file_name

file=file_name()
file_address='/home/baka/SentiMovie/Reviewcrawler/'+file
data=pd.read_csv(file_address)
if len(data.index)>2:
    print("Which one do you mean?")
    print(data['title'])
    index=input("Select an index")
else:
    index=0
    
column_titles=["title","released_date","overview","language","cast_members","crew_members","genres","budget","revenue","runtime","reviews"]
data=data.reindex(columns=column_titles)
data=data.rename(columns={'released_date':'release date','cast_members':'cast members','crew_members':'crew members','genres':'genre','reviews':'review'})

def cast_format():
    cast_detail={"actor_name":[],"actor_role":[]}
    castm=data.iat[int(index),4]
    castm=castm.split(",")
    switch=1
    
    for cast in castm:
        if switch%2!=0:
            cast_detail['actor_name'].append(cast)
        else:
            cast_detail['actor_role'].append(cast)
        switch+=1  
    mylist=cast_detail['actor_name']
    dict_detail = {un:[] for un in mylist}
    for r,c in zip(cast_detail['actor_name'],cast_detail['actor_role']):
        #print(r,c)
        dict_detail[r].append(c) 
    
    data.iat[int(index),4]=dict_detail
    



def crew_format():
    
    crew_detail={"crew_member":[],"crew_role":[]}
    crewd=data.iat[int(index),5]
    crewd=crewd.split(",")
    switch=1
    
    for crew in crewd:
        if switch%2!=0:
            crew_detail['crew_member'].append(crew)
        else:
            crew_detail['crew_role'].append(crew)
        switch+=1
    #print(crew_detail['crew_role'])
    #print(crew_detail['crew_member'])
    mylist=crew_detail['crew_role']
    used = set()
    unique = [x for x in mylist if x not in used and (used.add(x) or True)]
    dict_detail = {un:[] for un in unique}
    for r,c in zip(crew_detail['crew_member'],crew_detail['crew_role']):
        #print(r,c)
        dict_detail[c].append(r)        
    data.iat[int(index),5]=dict_detail
    

            
def review_format():
    review=data.iat[int(index),10]
    review=review.replace("A review by",'|')
    review=review+'|'
    count=0
    br_pos=[]
    rev=[]
    for r in review:
        count+=1
        if r=='|':
            br_pos.append(count)
    #print(br_pos)
    #print(review[br_pos[0]:br_pos[1]])
    ran=len(br_pos)
    try:
        for i in range(0,ran):
            revi=review[br_pos[i]:br_pos[i+1]]
            rev.append(revi)
    except IndexError:
        pass
    data.iat[int(index),10]=rev

def data_form():
    cast_format()
    crew_format()
    #review_format()
    data.to_csv(file)
    print("data formatting and exporting")
#data_form()