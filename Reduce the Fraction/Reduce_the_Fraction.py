def gcd(x, y):                      #function to find GCD
    while y != 0:
        (x, y) = (y, x % y)
    return x
    
n = int(input())                    #number of test cases
while n>0 :
    a,b=map(int,input().split())
    gcd = gcd(a,b)
    print(gcd)
    r1 = int(a/gcd)
    r2 = int(b/gcd)
    print("%d/%d"%(r1,r2))
    n-=1
