t = int(input())
while t>0:
    n,k=map(int,input().split())
    amount=0
    for i in range(k,n+1,k):
        amount+=i
    print(amount)
    t-=1
