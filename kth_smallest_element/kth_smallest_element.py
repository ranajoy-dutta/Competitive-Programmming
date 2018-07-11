# from TECHGIG
def main():
    n = int(input())
    arr=[]
    for i in range(n):
        arr.append(int(input()))
    v = int(input())
    arr = sorted(arr)
    print(arr[v-1])
    
main()


