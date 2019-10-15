n = int(input())
lst = []
for i in range(1,n+1):
    lst.append(i**i)
sum = 0
for j in range(0,n):
    sum = sum + lst[j]
res = [int(x) for x in str(sum)]

k = 0
for i in range(0,len(res)):
    if (i!=0):
        k = i
        break

ans = res[k+1:]
for i in ans:
    print(i, end = '')

