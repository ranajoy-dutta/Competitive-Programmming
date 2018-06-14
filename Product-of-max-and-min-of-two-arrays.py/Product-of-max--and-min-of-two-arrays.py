t = int(input())  # Number of test cases
while t > 0:  # while loop for test cases
    input()  # satisfying input format
    arr1 = list(map(int, input().split()))  # input first array
    input()  # satisfying input format
    arr2 = list(map(int, input().split()))  # input second array
    # printing result of product of maximum of first array and minimum of second array
    print(max(arr1) * min(arr2))
    t -= 1
