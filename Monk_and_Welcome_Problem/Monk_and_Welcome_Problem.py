t = int(input())
while t>0:
    try:
        arr1 = list(map(int,input().split()))
        arr2 = list(map(int,input().split()))
        for i in range(len(arr1)):
            print(arr1[i]+arr2[i], end=" ")
    except:
        print()
    t-=1
   
