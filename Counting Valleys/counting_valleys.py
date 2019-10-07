#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    #sea for sea level, valleyCount to keep count of valleys, flag to keep track if Gary came out of previous valley
    sea, valleyCount, flag = 0, 0, 0        
    s = list(s)             #converting string to list of letters (U, D)
    for i in s:             #looping over list
        if i=='U':          #check if its U(up) or D(down) 
            sea += 1
        else:
            sea -= 1
            
        if sea < 0 and flag == 0:   #if its first step below sealevel 
            valleyCount += 1
            flag = 1
        elif sea == 0 and flag == 1:    #reset flag if its first step above sealevel
            flag = 0
    return valleyCount
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
