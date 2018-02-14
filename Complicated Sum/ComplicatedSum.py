t=int(input())                           # test cases
mod=1000000007
while t>0:
    n=int(input())   
    res=(n*(n+1)*(3*n*n+7*n+2))//24
    print(res%mod)
    t=t-1
