# -*- coding: utf-8 -*-
"""
Project Euler - Problem 42
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so 
    the first ten triangle numbers are:
        1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
By converting each letter in a word to a number corresponding to its 
    alphabetical position and adding these values we form a word value. For 
    example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word 
    value is a triangle number then we shall call the word a triangle word.
Using words.txt (right click and 'Save Link/Target As...'), a 16K text file 
    of nearly two-thousand common English words, how many are triangle words?
"""

# Imports
import time
import math

# Initialise global variables
alph = {'A' :  1, 'B' :  2, 'C' :  3, 'D' :  4, 'E' :  5, 'F' :  6, 'G' :  7, 
        'H' :  8, 'I' :  9, 'J' : 10, 'K' : 11, 'L' : 12, 'M' : 13, 'N' : 14, 
        'O' : 15, 'P' : 16, 'Q' : 17, 'R' : 18, 'S' : 19, 'T' : 20, 'U' : 21, 
        'V' : 22, 'W' : 23, 'X' : 24, 'Y' : 25, 'Z' : 26}

# Functions
# Open file and read in words
def readNames(f_name):
    f = open(f_name, "r") 
    content = f.read()
    
    # Remove starting and trailing quotation marks
    content = content[1:-1]
    # Split line to separate names
    words = content.split('\",\"')
    f.close() # Close file
    return words

# Add a single element to array of triangular numbers
def buildTriangArr(arr):
    n = len(arr)
    arr.append(0.5*n*(n+1))
    return arr

# Check if a number is traiangular
def isTriangular(num):
    # n = (sqrt(1+8*num) - 1)/2
    n = (math.sqrt(1+8*num) - 1.0)/2.0
    if n == int(n):
        return True
    return False

# Get alphabetical score of a word
def wordScore(word):
    score = 0
    for i in range(0,len(word)):
        score += alph[word[i]]
    return score

# Get total words with triangular score
def fileScore(words):
    count = 0;
    
    for i in range(0,len(words)):
        score = wordScore(words[i])
        
        if isTriangular(score):
            count += 1
    
    return count

# Main function
def main():
    file_name = "textFiles/p042_words.txt"
    words = readNames(file_name)
    count = fileScore(words)
    
    print(count)
    
# To calculate prorgram run time
start = time.time()
main()
end = time.time()
print('Run time: {}'.format(end - start))    