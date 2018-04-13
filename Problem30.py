# -*- coding: utf-8 -*-
"""
Project Euler - Problem 30
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
    1634 = 14 + 64 + 34 + 44
    8208 = 84 + 24 + 04 + 84
    9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.
The sum of these numbers is 1634 + 8208 + 9474 = 19316.
Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

# Imports
import math 
import time
import sys

# Functions
# Create list of powers
def powerList(p):
    arr = list(range(0, 10))
    for a in arr:
        arr[a] = arr[a]**p
    return arr

# Get sum of digits to power of exponent
def digitPower(num, p, pow_list=[]):
    dig_sum = 0
    if pow_list == []:
        pow_list = powerList(p)
    
    for j in range(0,len(str(num))):
        dig_sum += pow_list[num%10]
        num = math.floor(num/10)    
    
    return dig_sum
    
# Get the maximum number to check for a given power
def findUpperBound(p):
    max_num = 9**p
    test_num = 1
    
    while test_num < max_num*len(str(test_num)):
        test_num *= 10
        
    return max_num*len(str(test_num-1))

# Find number that match digit power criteria
def sumDigitPowers(upper, p):
    pow_list = powerList(p) # List of digits raised to power
    digits = []
    dig_sum = 0
    
    for i in range(2,upper+1): # range(lower,upper+1):
        dig_sum = digitPower(i, p, pow_list)
        
        if dig_sum == i:
            digits.append(i)
            
    return sum(digits)

# Main function
def main():
    # Read exponent from command line, otherwise 5 by default
    if len(sys.argv) > 1 and isinstance(float(sys.argv[1]),float):
        power = int(math.floor(float(sys.argv[1])))
    else:
        power = 5
        
    # Execute code
    upper_b = findUpperBound(power)
    sum_digits = sumDigitPowers(upper_b, power)
    print('Sum of digits meeting criteria with power {}: {}'.format(power, sum_digits))  

# To calculate prorgram run time
start = time.time()
if __name__ == "__main__":
    main()
end = time.time()
print('Run time: {}'.format(end - start))  
