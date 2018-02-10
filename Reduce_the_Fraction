"""You are given a fraction - A/B.
Reduce the fraction to the lowest possible.

Input :: First line consist of T - the number of test cases. T lines follows - each consisting of 2 numbers A B.

Output :: Output T lines - In each line print the answer in the form P/Q. """

from fractions import Fraction      #importing library
def gcd(x, y):                      #function to find GCD
    while y != 0:
        (x, y) = (y, x % y)
    return x
    
n = int(input())                    #number of test cases
while n>0 :
    a,b=map(int,input().split())
    gcd = gcd(a,b)
    r1 = int(a/gcd)
    r2 = int(b/gcd)
    print("%d/%d"%(r1,r2))
    n-=1
