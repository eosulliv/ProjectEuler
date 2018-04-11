# -*- coding: utf-8 -*-
"""
Project Euler - Problem 15
Lattice Paths:
Starting in the top left corner of a 2×2 grid, and only being able to move to 
    the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
"""

# Imports
import time

# Functions
# Find number of paths recursively - brute force
def recPath(grid_size):
    # reached corner, no moves left
    if grid_size == [0,0]: return 1
    # recursive calls
    paths = 0
    # move left when possible
    if grid_size[0] > 0:
        paths += recPath([grid_size[0]-1,grid_size[1]])
    # move down when possible
    if grid_size[1] > 0:
        paths += recPath([grid_size[0],grid_size[1]-1])
 
    return paths

# Find number of paths recursively - smart recurse
#                                                      1  1  1  1
#                                                    |-----------
#       1                  if j = 0                1 | 2  3  4  5
# Sij = Si,j-1 + Si-1,j    if 0 < i < j            1 | 3  6 10 15
#       2Si,j-1            if i = j                1 | 4 10 20 35
#                                                  1 | 5 15 35 70
# Inspired by http://code.jasonbhill.com/python/project-euler-problem-15/
def recPathSmart(grid_size):
    arr = list(range(2, grid_size[0]+2))
    # print(arr)
    
    for i in range(0,grid_size[0]-1):
        for j in range(0, grid_size[1]):
            if j == 0:
                arr[0] += 1
            else:
                arr[j] += arr[j-1]
            
        # print(arr, arr[0], arr[-1])
                
    return arr[-1]

# To calculate prorgram run time
start = time.time()

# Initialise variables
grid_size = [20, 20]

# Call code
num_paths = recPathSmart(grid_size)

end = time.time()
print('Run time: {}'.format(end - start))   
print('Num paths: {}'.format(num_paths))