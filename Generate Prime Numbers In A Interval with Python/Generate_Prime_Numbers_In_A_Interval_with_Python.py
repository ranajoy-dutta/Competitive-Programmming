''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    n1 = int(input())
    n2 = int(input())
    for i in range(n1, n2):
        if i>1:
            prime = True
            for j in range(2, i):
                if i%j == 0:
                    prime = False
                    break
            if prime:
                print(i)
    return True

main()

