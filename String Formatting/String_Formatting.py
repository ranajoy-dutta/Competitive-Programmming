def print_formatted(number):
    w =len(bin(number)[2:])
    for i in range(1,number+1):
        print (str(i).rjust(w,' '),oct(i)[2:].rjust(w,' '),hex(i)[2:].upper().rjust(w,' '),bin(i)[2:].rjust(w,' '))
