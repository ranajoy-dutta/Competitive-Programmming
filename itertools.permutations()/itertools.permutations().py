from itertools import permutations
string, n = map(str,input().split())
listt = sorted(list(permutations(string,int(n))))
for i in listt:
    for j in i:
        print(j,end="")
    print()
