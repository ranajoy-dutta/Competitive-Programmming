def diagonalDifference(arr):
    v_sum = 0
    lcounter = 0
    rcounter = len(arr[0])-1
    for i in arr:
        v_sum = v_sum + i[lcounter] - i[rcounter]
        lcounter+=1
        rcounter-=1
    return abs(v_sum)


n = int(input().strip())
a = []
for a_i in range(n):
   a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
   a.append(a_t)
result = diagonalDifference(a)
print(result)
