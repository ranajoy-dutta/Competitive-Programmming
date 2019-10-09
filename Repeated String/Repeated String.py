#!/bin/python3

import math
import os
import random
import re
import sys


# logic used :: find number of a in original string, multiply that to n. If length of string is not a factor of n, then find number of a in its subtring.
# Complete the repeatedString function below.
def repeatedString(s, n):             
    countA = 0              
    for i in list(s):               #counting 'a' in string
        if i == 'a':
            countA += 1
    total = (n//len(s))*countA      #multiply number of 'a' in string to n
    sub = n%len(s)
    for i in range(0, sub):         #find 'a' if its in substring of that string
        if s[i] == 'a':             
            total += 1
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
