n = int(input())
big_arr=[]
while n>0:
    arr = list(map(str, input().split()))
    big_arr.append(arr)
    n-=1
name = input()
lst = []
for i in range(len(big_arr)):
    if big_arr[i][0]==name:
        lst=big_arr[i]
sum=0
for i in range(1,len(lst)):
    sum = sum + float(lst[i])
print("%.2f"%(sum/3))

# Created by rupali
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = str(input())
if query_name in student_marks:
    l=list(student_marks[query_name])
    sum=0
    for i in range(len(l)):
     sum= l[i]+sum
print("{:.2f}".format(sum/3))
