from itertools import combinations
input()
arr = input().split()
k = int(input())
total,count = 0,0
for i in combinations(arr,k):
    total += 1
    for j in i:
        if j == 'a':
            count += 1
            break
print(count/total)
