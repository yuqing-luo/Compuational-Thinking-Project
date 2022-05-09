#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  3 16:10:37 2021

@author: cherry
"""
import pandas as pd
import matplotlib.pyplot as plt
import csv

channel_dict = {}

def mostPopularChannel(): 
    
    df = pd.read_csv('USvideos.csv')
    df.to_dict('list')
    for channel in df['channel_title']:
        if channel in channel_dict:
            channel_dict[channel] += 1
        else:
            channel_dict[channel] = 1
            
    return [channel for channel,amount in channel_dict.items() if amount == max(channel_dict.values())]
    