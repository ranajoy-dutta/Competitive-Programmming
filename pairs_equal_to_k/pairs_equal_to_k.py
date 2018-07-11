# from TECHGIG
def main():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(int(input()))
    v = int(input())
    arr = sorted(arr)
    count=0
    for i in range(n-1):
        for j in range(i+1,n):
            if (arr[j]-arr[i])==v:
                count+=1
    print(count)
main()
