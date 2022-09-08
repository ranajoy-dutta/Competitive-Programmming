#!/bin/python3


def plusMinus(arr):
    n = len(arr)
    positives, negetives, zeroes = 0, 0, 0
    for ele in arr:
        if ele > 0:
            positives += 1
        elif ele < 0:
            negetives += 1
        else:
            zeroes += 1
    print("{:.6f}".format(round(positives/n, 6)))
    print("{:.6f}".format(round(negetives/n, 6)))
    print("{:.6f}".format(round(zeroes/n, 6)))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
