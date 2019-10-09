#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    n=len(c)
    jumps, pos = 0, 0
    while pos < n - 1:
        if pos + 2 >= n or c[pos + 2] == 1:
            pos = pos + 1
            jumps = jumps + 1
        else:
            pos = pos + 2
            jumps = jumps + 1
    return jumps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
