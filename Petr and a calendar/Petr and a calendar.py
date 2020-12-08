''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    # for _ in range(int(input())):
    month = int(input())
    first_day = int(input())
    # all months except feb will need atleast 5 columns. More columns may be required 
    # depending on first day of the month.
    more_columns = first_day - 1
    if month==2:
        print(5 if first_day>1 else 4)
    elif month in [1,3,5,7,8,10,12]:
        print(6 if first_day>4 else 5)
    else:
        print(6 if first_day>5 else 5)
    return True

main()

