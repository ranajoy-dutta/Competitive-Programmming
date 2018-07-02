t=int(input())
while t>0:
    n = int(input(""))
    counter=7
    term=1
    while term<n:
            counter = counter+counter+term
            term+=1
    print(counter%((10**9)+7))
    t-=1
