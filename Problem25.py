# -*- coding: utf-8 -*-
'''
Project Euler - Problem 25
Calculate first number in Fibonacci sequence to contain 1000 digits
F(n) = F(n-1) + F(n-2)
F(0) = 0, F(1) = 1, F(2) = 1
'''

# Imports
import time

# To calculate prorgram run time
start = time.time()

# Initialise variables
num_digits = 1000
a = 1
b = 0
n = 1

# Loop until desired digit length is achieved
while len(str(a)) < num_digits:
    a, b = a+b, a
    n += 1
    
end = time.time()
print('Run time: {}'.format(end - start))    
print('Number: {} \nLength: {} \nTerm in sequence: {}'.format(a, len(str(a)), n))
