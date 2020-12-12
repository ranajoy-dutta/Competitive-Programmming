''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    n = int(input())
    k = int(input())
    if n%k==0:
        print(n+k)
    else:
        mid = int(-(-(n/k) // 1)) # you can use math.ceil
        print(k*mid)

main()

