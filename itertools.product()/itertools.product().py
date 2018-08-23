from itertools import product
result = list(product(tuple(map(int,input().split())),tuple(map(int,input().split()))))
for i in result:
    print(i, end=" ")
