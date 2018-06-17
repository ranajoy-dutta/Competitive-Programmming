t = int(input())
while t>0:
    input()
    arr = list(map(int,input().split()))
    x = int(input())
    first,last = -1,-1
    for i in range(len(arr)):
        if arr[i] == x:
            if first == -1:
                first,last=i,i
            else:
                last = i
    if first == -1:
        print(first)
    else:
        print(first,last)
    t -= 1