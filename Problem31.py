# -*- coding: utf-8 -*-
"""
Project Euler - Problem 31
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:
    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""

# Imports
import math
import sys
import time

# Functions
def main():
    # Read quantity from command line, otherwise 2 pounds by default
    if len(sys.argv) > 1 and isinstance(float(sys.argv[1]),float):
        quant = float(sys.argv[1])
    else:
        quant = 2
    
    quant = quant*100 # Assuming quantity is entered in pounds
    coin_sum = 0
        
    c = [200, 100, 50, 20, 10, 5, 2, 1]
    
    for two_h in range(int(math.floor(quant)),-1,-c[0]):
        for one_h in range(two_h,-1,-c[1]):
            for fifty in range(one_h,-1,-c[2]):
                for twenty in range(fifty,-1,-c[3]):
                    for ten in range(twenty,-1,-c[4]):
                        for five in range(ten,-1,-c[5]):
                            for two in range(five,-1,-c[6]):
                                coin_sum += 1
    
    print('Ways in which {}p can be made up using coings: {}'.format(int(quant), coin_sum))  

# To calculate prorgram run time
start = time.time()
if __name__ == "__main__":
    main()
end = time.time()
print('Run time: {}'.format(end - start))    
