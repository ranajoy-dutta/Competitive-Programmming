## Collection Named-tuple
> **Named tuples assign meaning to each position in a tuple and allow for more readable, self-documenting code.<br/> They can be used wherever regular tuples are used, and they add the ability to access fields by name instead of position index.
You are given a data containing test results of class. The dataset consists of two columns namely : 'marks' and 'name'.<br/> These two Columns can be in any order i.e. ('name' followed by 'marks' or vice versa).
You have to find the average marks for the whole class.**

**Input Format**<br/>
First line will contain an Integer N, denoting the number of students.<br/>
Next line will contain two string denoting the column heading.<br/>
Next N lines will contain marks and name of the students respective of column headings.<br/>


**Constraints**<br/>
1 <= N <= 10^3<br/>
0 <= Marks <= 100<br/><br/>

**Output Format** <br/>
Output the average marks of the class rounded off to two decimal places.

**Sample Input**<br/>
3<br/>
marks names<br/>
10 arpit<br/>
20 anushka<br/>
35 rakshita<br/><br/>

**Sample Output**<br/>
21.67