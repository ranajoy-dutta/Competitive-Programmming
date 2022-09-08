#!/bin/python3

def miniMaxSum(arr):
    v_min, v_max, v_sum =  arr[0], arr[0], 0
    for ele in arr:
        if ele < v_min:
            v_min = ele
        if ele > v_max:
            v_max = ele
        v_sum += ele
    print(v_sum-v_max, v_sum-v_min)


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
