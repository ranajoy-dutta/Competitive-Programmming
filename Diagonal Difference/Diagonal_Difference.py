"""Given a square matrix of size , calculate the absolute difference between the sums of its diagonals.

Input Format :: The first line contains a single integer, . The next  lines denote the matrix's rows, with each line containing space-separated integers describing the columns.

Output Format :: Print the absolute difference between the two sums of the matrix's diagonals as a single integer.

Sample Input
3
11 2 4
4 5 6
10 8 -12

Sample Output
15
"""
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
