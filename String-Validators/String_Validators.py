if __name__ == '__main__':
    s = input()
    alnum,num,cap,low,al = 'False','False','False','False','False'
    for i in s:
        if i.isalnum():
            alnum = "True"
        if i.isalpha():
            al = "True"
        if i.isdigit():
            num = "True"
        if i.islower():
            low = "True"
        if i.isupper():
            cap = "True"
print(alnum)
print(al)
print(num)
print(low)
print(cap)
