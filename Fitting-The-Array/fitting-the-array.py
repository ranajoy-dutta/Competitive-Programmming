t = int(input())
while t>0:
    input()
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))
    arr1.sort()
    arr2.sort()
    flag = 0
    for i in range(len(arr1)):
        if arr1[i]>arr2[i]:
            flag = 1
    if flag==1:
        print("NO")
    else: 
        print("YES")
    
    t-=1
