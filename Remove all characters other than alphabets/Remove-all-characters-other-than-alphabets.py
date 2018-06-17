import string

t = int(input())
while t > 0:
    str1 = input()
    str2 = ''
    for i in str1:
        if i in string.ascii_lowercase or i in string.ascii_uppercase:
            str2 = str2 + i
    if str2!='':
        print(str2)
    else:
        print('-1')
    t -= 1
