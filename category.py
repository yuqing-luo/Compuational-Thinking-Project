#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  3 23:19:12 2021

@author: cherry
"""
import pandas as pd
import json

df = pd.read_csv("USvideos.csv")

def getCategory():

    with open("US_category_id.json") as f:
            categories = json.load(f)["items"]
            cat_dict = {}
            for cat in categories:
                cat_dict[int(cat["id"])] = cat["snippet"]["title"]
                df['category_name'] = df['category_id'].map(cat_dict)

    return(cat_dict)