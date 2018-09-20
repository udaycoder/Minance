#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 22:06:21 2018

@author: udaycoder
"""

import datetime
import requests, zipfile, io

def isLeapYear(year):
    if((year%400 == 0) or (year%100!=0 and year%4==0)):
        return  True
    else:
        return False

now = datetime.datetime.now()

curr_year = int(now.year)
curr_month = int(now.month)
curr_day = int(now.day)
day_of_week = datetime.datetime.today().weekday()

days = [31,28,31,30,31,30,31,31,30,31,30,31]
month = ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]

days_in_year = 365

curr_day -=1
if(curr_day == 0):
   curr_month -= 1
   if(curr_month == 0):
       curr_month = 12
       curr_year -= 1
   if(curr_month == 2):
       if(isLeapYear(curr_year)):
           curr_day = 29
       else:
           curr_day = 28
   else:
       curr_day = days[curr_month-1]

fout=open("minance3output/minance3output.csv","a")

while(days_in_year>0):
    try:
        file_str = "cm" + str(curr_day) + str(month[curr_month-1]) + str(curr_year) + "bhav.csv.zip"
        url_str = "https://nseindia.com/content/historical/EQUITIES/"+str(curr_year)+"/"+str(month[curr_month-1])+"/" + file_str
        r = requests.get(url_str)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall("minance3output/")
        print("Running ",curr_day," ",month[curr_month-1]," ",curr_year)
        f_path = "minance3output/"+ "cm" + str(curr_day) + month[curr_month-1] + str(curr_year) + "bhav.csv"
        f = open(f_path)
        if(days_in_year!=365):
            header = f.readline()
        for line in f:
            fout.write(line)
        f.close()
    except:
        print("NSE Closed on ",curr_day," ",month[curr_month-1]," ",curr_year," - Skipping!")
    day_of_week -=1
    if(day_of_week == -1):
        day_of_week = 6
    days_in_year -=1
    curr_day -=1
    if(curr_day == 0):
        curr_month -= 1
        if(curr_month == 0):
            curr_month = 12
            curr_year -= 1
        if(curr_month == 2):
            if(isLeapYear(curr_year)):
                curr_day = 29
            else:
                curr_day = 28
        else:
            curr_day = days[curr_month-1]

fout.close()