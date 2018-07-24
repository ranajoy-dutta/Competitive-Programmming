n = int(input())
big_arr = []
while n>0:
    name = input()
    marks = float(input())
    big_arr.append([marks,name])
    big_arr = sorted(big_arr)
    n-=1
smallest = big_arr[0][0]

pos=[]
for i in range(len(big_arr)):
    if big_arr[i][0]==smallest:
        pos.append(i)

for index in sorted(pos, reverse=True):
    del big_arr[index]
    
smallest = big_arr[0][0]

for i in range(len(big_arr)):
    if big_arr[i][0]==smallest:
        print(big_arr[i][1])


