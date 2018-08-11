## Lists
> **Consider a list (list = []). You can perform the following commands:<br/>

1. insert i e: Insert integer  at position .<br/>
2. print: Print the list.<br/>
3. remove e: Delete the first occurrence of integer .<br/>
4. append e: Insert integer  at the end of the list.<br/>
5. sort: Sort the list.<br/>
6. pop: Pop the last element from the list.<br/>
7. reverse: Reverse the list.<br/>

Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.**

**Input Format**<br/>
The first line contains an integer, n, denoting the number of commands. <br/>
Each line i of the n subsequent lines contains one of the commands described above.<br/>

**Output Format** <br/>
For each command of type print, print the list on a new line.<br/>

**Constraints**<br/>
The elements added to the list must be integers.<br/>

**Sample Input**<br/>
12<br/>
insert 0 5<br/>
insert 1 10<br/>
insert 0 6<br/>
print<br/>
remove 6<br/>
append 9<br/>
append 1<br/>
sort<br/>
print<br/>
pop<br/>
reverse<br/>
print<br/>

**Sample Output**<br/>
[6, 5, 10]<br/>
[1, 5, 9, 10]<br/>
[9, 5, 1]