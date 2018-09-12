from itertools import combinations
string, n = map(str,input().split())

for i in range(1,int(n)+1):
    listt = list(combinations(string,i))
    for j in range(len(listt)):
        listt[j] = sorted(listt[j])
    for j in sorted(listt):
        for k in j:
            print(k, end="")
        print()