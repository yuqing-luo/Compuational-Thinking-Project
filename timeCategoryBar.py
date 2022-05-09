#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 19:52:15 2021

@author: cherry
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import category as c

dict_2017 = {}
dict_2018 = {}
cat_dict = c.getCategory()

def timeCategoryBar():
    
    with open('USvideos.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if row['publish_time'][:4] == '2017':
                if row['category_id'] in dict_2017:
                    dict_2017[row['category_id']] += 1
                else:
                    dict_2017[row['category_id']] = 1
                    
            if row['publish_time'][:4] == '2018':
                if row['category_id'] in dict_2018:
                    dict_2018[row['category_id']] += 1
                else:
                    dict_2018[row['category_id']] = 1
                    
        return dict(sorted(dict_2017.items(), key=lambda item: item[1])),dict(sorted(dict_2018.items(), key=lambda item: item[1]))
                    
cat2017 = {}
cat2018 = {}
dict_2017 = timeCategoryBar()[0]
dict_2018 = timeCategoryBar()[1]
    
def getCat2017():
    for video in dict_2017:
        for cat in cat_dict:
            if str(cat) == video:
                cat2017[cat_dict[cat]] = dict_2017[video]
    
    return dict(sorted(cat2017.items(), key=lambda item: item[1]))

def getCat2018():
    for video in dict_2018:
        for cat in cat_dict:
            if str(cat) == video:
                cat2018[cat_dict[cat]] = dict_2018[video]
    
    return dict(sorted(cat2018.items(), key=lambda item: item[1]))

newcat2017 = getCat2017()
cat2018 = getCat2018()

w = 0.4

x = ['People & Blogs', 'Comedy', 'Howto & style', 'Music', 'Entertainment']
cat_2017 = [1724, 1984, 1958, 3338, 5014]
cat_2018 = [4656, 4914, 6326, 9570, 14814]

bar1 = np.arange(len(x))
bar2 = [i+w for i in bar1]

plt.bar(bar1, cat_2017, w, label = '2017')
plt.bar(bar2, cat_2018,w,label='2018' )

plt.xlabel('Category')
plt.ylabel('Amount')
plt.title('2017 vs 2018 categories comparison')
plt.xticks(bar1,x)
plt.legend()
plt.show()

                
              
    
    