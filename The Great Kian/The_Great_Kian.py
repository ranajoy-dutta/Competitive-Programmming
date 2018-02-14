n = int(input().strip())
a = [int(x) for x in input().strip().split()]         
print("{} {} {}".format(sum(a[::3]),sum(a[1::3]),sum(a[2::3])))
