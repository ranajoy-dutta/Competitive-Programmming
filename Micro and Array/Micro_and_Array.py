for i in range(int(input())):                #For test cases
    n, k = map(int, input().split(' '))      #input N and K
    l = min(map(int, input().split(' ')))    #input array and finding least in array
    if l < k:                                #finding least number of seconds
        print(k - l)
    else: 
        print(0)
