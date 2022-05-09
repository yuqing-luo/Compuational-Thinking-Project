#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  3 19:42:35 2021

@author: cherry
"""

import pandas as pd
import matplotlib.pyplot as plt
import csv
from datetime import date

trendingDays = {}

def OldestTrending():
    with open('USvideos.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            d0_removed = row['publish_time'][:10]
            d0_list = d0_removed.split("-")
            d0 = date(int(d0_list[0]), int(d0_list[1]), int(d0_list[2]))
            d1_list = row['trending_date'].split(".")
            d1 = date(int('20'+d1_list[0]), int(d1_list[2]), int(d1_list[1]))
            delta = d1-d0
            if row['title'] not in trendingDays:
                trendingDays[row['title']] = delta
            else: 
                if delta > trendingDays[row['title']]:
                    trendingDays[row['title']] = delta
        
        return [name for name,trending in trendingDays.items() if trending == max(trendingDays.values())], trendingDays['Budweiser - Original Whazzup? ad']
    