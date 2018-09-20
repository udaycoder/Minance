#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 23:30:07 2018

@author: udaycoder
"""

import pandas as pd

df=pd.read_csv('minance3output/minance3output.csv',low_memory=False)
df.drop_duplicates(subset=None, keep='first', inplace=False)
count_row=df.shape[0]
print("Number of unique records in cssv is: ",count_row)
df.to_csv('minance4output.csv')


