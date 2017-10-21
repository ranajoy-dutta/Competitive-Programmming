''' Given an array of integers where each element represents the max number of steps that can be made forward from that element. 
Write a function to return the minimum number of jumps to reach the end of the array (starting from the first element). 
If an element is 0, then cannot move through that element.

Input: 
The first line contains an integer T, depicting total number of test cases. 
Then following T lines contains a number n denoting the size of the array. Next line contains the sequence of integers a1, a2, ..., an.

Output:
Each seperate line showing the minimum number of jumps. If answer is not possible print -1.

Constraints:
1 ≤ T ≤ 40
1 ≤ N ≤ 100
0<=a[N]<=100

Example:
Input:
1
11
1 3 5 8 9 2 6 7 6 8 9

Output:
3         '''

#Solution

n=int(input().strip())
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
for _ in range(n):
    a_size=int(input().strip())
    p=input().strip()
    a=list(map(int,p.split(" ")))
    m=minstep(a,a_size)
    if(m==10000):
        print(-1)
    else:
        print(m)
