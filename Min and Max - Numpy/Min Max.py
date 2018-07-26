import numpy
n = list(map(int,input().split()))
n = n[0]
for i in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)
mins = numpy.min(arr, axis = 1)
print(max(mins))
        

