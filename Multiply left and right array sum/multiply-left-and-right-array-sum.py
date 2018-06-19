t = int(input())
while t>0:
    n=int(input())
    arr = list(map(int,input().split()))
    sum1,sum2 =0,0
    for i in range(0,n//2):
        sum1 += arr[i]
    for i in range(n//2,n):
        sum2 += arr[i]
    print(sum1*sum2)
    t -= 1
