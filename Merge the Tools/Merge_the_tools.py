def rem_duplicate(string):
    result = []
    for c in string:
        if c not in result:
            result.append(c)
    return ''.join(result)

def merge_the_tools(string, k):
    a=0
    for i in range(len(string)//k):
        print(rem_duplicate(string[a:a+k]))
        a+=k
