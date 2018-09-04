from collections import Counter
n = int(input())
mylist = list(map(int, input().split()))
counter = Counter(mylist)
q = int(input())
total=0
while q>0:
    val = map(int, input().split()))
    size_qty = counter.get(val[0])
    if size_qty != 0 and size_qty != None:
        counter[val[0]]=(counter.get(val[0])-1)
        total+=val[1]
    q -= 1
print(total)
