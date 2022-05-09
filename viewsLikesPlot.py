#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  3 17:30:18 2021

@author: cherry
"""
import pandas as pd
import matplotlib.pyplot as plt
import csv

channel_dict = {}

def viewsLikesPlot(): 
    
    df = pd.read_csv('USvideos.csv')
    df.to_dict('list')
    x = df['views']
    y = df['likes']
    
    plt.scatter(x,y)
    plt.xlabel('views')
    plt.ylabel('likes')
    plt.title('Youtube trending video likes vs. views')
    plt.show()
    


    
    
    
