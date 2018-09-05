from itertools import combinations_with_replacement
string, n = map(str, input().split())

listt = list(combinations_with_replacement(string,int(n)))
for i in range(len(listt)):
    listt[i] = sorted(listt[i])
    
for i in sorted(listt):
    for j in i:
        print(j, end="")
    print()