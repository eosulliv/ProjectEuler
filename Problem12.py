# -*- coding: utf-8 -*-
"""
Project Euler - Problem 12
Highly divisible triangular numbers:
What is the value of the first triangle number to have over five hundred divisors?
"""

# Imports
import time
import math 

# Lamda functions
triang = lambda n: (n*(n+1))/2

# Functions
# Get number of divisors in variable
def getNumDivs(n):    
    if n == 1:
        return 1
    else:    
        divs = 0
        n = math.floor(int(n))
        for i in range (1, math.floor(math.sqrt(n))+1):
            if n%i == 0:
                divs += 2
    return divs

# To calculate prorgram run time
start = time.time()

# Initialise variables
n = 1       # nth term in sequence
fn = 1      # nth triangular number
divs = 0    # number of divisors

# Loop until required number of divisors found
while divs < 500:
    fn = triang(n) 
    divs = getNumDivs(fn)
    n += 1

end = time.time()
print('Run time: {}'.format(end - start))    
print('Number: {} \nDivisors: {} \nTerm in sequence: {}'.format(fn, divs, n))