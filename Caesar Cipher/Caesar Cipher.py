#!/bin/python3

import os

def caesarCipher(s, k):
    encr_string = ''
    for letter in s:
        if letter.isalpha():    
            uni = ord(letter)
            base = 97 if letter.islower() else 65
            balance = (uni + k - base) % 26
            encr_string += chr(balance + base)  # adding base to bring in alphabet range
        else:
            encr_string += letter
    return encr_string

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
