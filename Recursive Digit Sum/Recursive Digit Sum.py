#!/bin/python3

import os


def superDigit_rec(n):
    if int(n)<10:
        return n
    else:
        s = sum([int(x) for x in str(n)])
        return superDigit_rec(s)


def superDigit(n, k):
    l = int(superDigit_rec(n)*k)
    return superDigit_rec(l)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
