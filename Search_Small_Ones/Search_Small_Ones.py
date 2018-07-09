# from TECHGIG
def main():
    n = int(input())
    arr = list(map(int,input().split()))
    min1 = min(arr)
    arr.remove(min1)
    print(min(arr) + min1)

main()

