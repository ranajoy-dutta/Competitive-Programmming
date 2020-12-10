''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    m = int(input())
    d = int(input())
    counter, col = 1, 1
    days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    
    while (counter<days[m]):
        counter += 1
        d += 1
        if (d>7):
            d = 1
            col += 1
    print(col)

main()


