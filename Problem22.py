# -*- coding: utf-8 -*-
"""
Project Euler - Problem 22
Using names.txt, a 46K text file containing over five-thousand first names, 
    begin by sorting it into alphabetical order. Then working out the 
    alphabetical value for each name, multiply this value by its alphabetical 
    position in the list to obtain a name score.
For example, when the list is sorted into alphabetical order, COLIN, which is 
    worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN 
    would obtain a score of 938 × 53 = 49714.
What is the total of all the name scores in the file?
"""

# Imports
import time

# Functions
# Open file and read in names
def readNames(f_name):
    # Open file and read names
    f = open(f_name, "r") 
    content = f.read()
    # line = f.readline()
    # line = line[0:102]
    
    # Remove starting and trailing quotation marks
    content = content[1:-1]
    # Split line to separate names
    names = content.split('\",\"')
    # Close file
    f.close()
    return names

# Sort names in alphabetical order
def sortNames(names):
    names = sorted(names)
    return names        

# Get total name value based on array index
def fileScore(names):
    score = 0;
    for i in range(0,len(names)):
        score += (i+1.0)*nameScore(names[i])
        if i == 937:
            print((i+1.0)*nameScore(names[i]))
    return score

# Get value of a passed name
def nameScore(name):
    score = 0
    for i in range(0,len(name)):
        score += alph[name[i]]
    return score

# To calculate prorgram run time
start = time.time()

# Initialise variables
file_name = "textFiles/p022_names.txt"
file_score = 0
alph = {'A' :  1, 'B' :  2, 'C' :  3, 'D' :  4, 'E' :  5, 'F' :  6, 'G' :  7, 
        'H' :  8, 'I' :  9, 'J' : 10, 'K' : 11, 'L' : 12, 'M' : 13, 'N' : 14, 
        'O' : 15, 'P' : 16, 'Q' : 17, 'R' : 18, 'S' : 19, 'T' : 20, 'U' : 21, 
        'V' : 22, 'W' : 23, 'X' : 24, 'Y' : 25, 'Z' : 26}

# Execute code
names = readNames(file_name)
names = sortNames(names)
file_score = fileScore(names)

end = time.time()
print('Run time: {}'.format(end - start))    
print('Total name values: {}'.format(file_score))
