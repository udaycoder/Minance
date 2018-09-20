#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 19:43:07 2018

@author: udaycoder
"""
def isLeapYear(year):
    if((year%400 == 0) or (year%100!=0 and year%4==0)):
        return  True
    else:
        return False
    
def findNumberOfExtraDays(year):
    count = 0;
    if(year>2000):
        for i in range(2001,(year+1)):
            if(isLeapYear(i)):
                count+=2
            else:
                count+=1
    elif(year<2000):
        for i in range((year+1),2001):
            if(isLeapYear(i)):
                count+=2
            else:
                count+=1
    return count

def dayOfExtraDay(year):
    day = ["Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday","Monday"]
    revDay = ["Tuesday","Monday","Sunday","Saturday","Friday","Thursday","Wednesday"]
    currIn = 0;
    if(year==2000):
        return day[currIn]
    elif(year>2000):
        currIn = findNumberOfExtraDays(year) % 7
        return day[currIn]
    elif(year<2000):
        currIn = findNumberOfExtraDays(year)%7
        return revDay[currIn]
        
    

year = int(input("Input: "))
print("Output: ")
if(isLeapYear(year)):
    print(dayOfExtraDay(year))
else:
    print("This is not a leap year")
    year1=year
    while(True):
        year1+=1
        if(isLeapYear(year1)):
            break
    d1 = year1-year
    year2=year
    while(True):
        year2-=1
        if(isLeapYear(year2)):
            break
    d2 = year-year2
    if(d1==d2):
        print("There are two leap years equidistant from current leap year")
        print(year1," ",dayOfExtraDay(year1))
        print(year2," ",dayOfExtraDay(year2))
    elif(d1<d2):
        print("Closest leap year: ",year1)
        print(dayOfExtraDay(year1))
    elif(d1>d2):
        print("Closest leap year: ",year2)
        print(dayOfExtraDay(year2))