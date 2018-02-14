def diagonalDifference(a):
    difference = sum(row[i] - row[-i-1] for i, row in enumerate(a))
    return abs(difference)

n = int(input().strip())
a = []
for a_i in range(n):
   a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
   a.append(a_t)
result = diagonalDifference(a)
print(result)
