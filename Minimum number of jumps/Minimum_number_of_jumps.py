def minstep(a,a_size):
    x=[10000 for _ in range(a_size)]
    if(a[0]==0):
        return -1
    else:
        x[0]=0
        for i in range(0,a_size):
            z=min(i+a[i],a_size-1)
            for j in range(i+1,z+1):
                if(x[i]+1<x[j]):
                    x[j]=x[i]+1
    return x[a_size-1]

a_size=int(input().strip())
p=input().strip()
a=list(map(int,p.split(" ")))
m=minstep(a,a_size)
if(m==10000):
    print(-1)
else:
    print(m)
