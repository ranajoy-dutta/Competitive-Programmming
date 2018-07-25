n = int(input())
big_arr=[]
while n>0:
    arr = list(map(str, input().split()))
    big_arr.append(arr)
    n-=1
name = input()
lst = []
for i in range(len(big_arr)):
    if big_arr[i][0]==name:
        lst=big_arr[i]
sum=0
for i in range(1,len(lst)):
    sum = sum + float(lst[i])
print("%.2f"%(sum/3))
