def main():
    n = int(input())
    input()
    summ = 0
    for i in range(n):
        marks,name = input().split()
        summ+=int(marks)
    print("{0:.2f}".format(summ/n))
main()

