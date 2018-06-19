t = int(input())
while t>0:
    num = input()
    arr=[]
    score=0
    for i in range(len(num)):
        if num[i]=='2':
           score+=int(num[i+1])
    print(score)
    t -= 1
