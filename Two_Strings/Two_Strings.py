t = int(input())
while t>0:
    a,b=map(str,input().split())
    flag=1
    for i in b:
         if i in a:
              a=a.replace(i,"")
    if a=="":
         print("YES")
    else:
         print("NO")
    t-=1
