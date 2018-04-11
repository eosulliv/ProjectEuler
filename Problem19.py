# -*- coding: utf-8 -*-
"""
Project Euler - Problem 19
You are given the following information, but you may prefer to do some research for yourself.
    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

# Imports
import time
from datetime import date

# Lamda functions

# Functions
def numSundays(start_y, end_y):
    days = getStartDay(start_y)
    sundays = 0
    
    for year in range(start_y, end_y+1):
        for mth in range(0,len(months)):
            # Check if months is February
            if(mth==1 and (year%4==0 and year%100!=0 or year%400==0)):
                days += 29
            else:
                days += months[mth]
                
            if days%7 == 0:
                sundays += 1
    
    return sundays

# Get day of the week a given year started on
# 0 = Sunday, 1 = Monday, 2 = Tuesday, etc...
def getStartDay(start_y):
    # 1/1/1900 given to be a Monday
    days = (date(start_y,1,1) - date(1900,1,1)).days 
    return (1 + days)%7
    
# To calculate prorgram run time
start = time.time()

# Initialise variables
num_sundays = 0
start_year = 1901
end_year = 2000
months = [ 31, # January
           28, # February
           31, # March
           30, # April
           31, # May
           30, # June
           31, # July
           31, # August
           30, # September
           31, # October
           30, # Novemeber
           31, # December
          ]

# Execute code
num_sundays = numSundays(start_year, end_year)

end = time.time()
print('Run time: {}'.format(end - start))
print('Number of Sundays between {} and {} that fall on the 1st of the month: {}'.format(start_year, end_year, num_sundays))