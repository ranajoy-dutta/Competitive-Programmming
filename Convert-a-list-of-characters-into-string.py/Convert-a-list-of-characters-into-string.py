t = int(input())  # Number of test cases
while t > 0:
    input()         # satisfying input format
    val = list(map(str, input().split())) # Input Multiple characters in one line
    res = ''
    for i in range(len(val)):       # for loop to create string from list of characters
        res = res + str(val[i])
    print(res)      # Printing the resultant string
    t -= 1
