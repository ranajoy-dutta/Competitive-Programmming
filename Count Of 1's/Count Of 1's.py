''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    counter = 0
    for _ in range(int(input())):
        if int(input())==0:
            break
        counter+=1

    print(counter)
main()

