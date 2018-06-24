## Fitting The Array
> **Adobe is playing an array game. He is weak in the concepts of arrays. Adobe is given two arrays a[ ] and b[ ] of the same size. The array a[ ] will be said to fit in array b[ ] if by arranging the elements of both array, there exists a solution such that i_th element of a[ ] is less than or equal to an i_th element of b[ ]. Help Adobe find if the given arrays are fit or not.**

**Input Format**<br/>
The first line of input contains an integer T denoting the number of test cases. For each test case, the next subsequent line contains the integer N i.e. size of arrays followed by array a[ ] and then array b[ ].

**Output Format** <br/>
Print "YES" if array a[ ] fit in array b[ ] otherwise print "NO".

**Constraints**<br/>
1<= T<= 100<br/>
1<= N<= 100<br/>
0<=a[ i ]<=1000<br/>
0<= b[ i ]<=1000<br/>

**Sample Input**<br/>
2<br/>
4<br/>
7 5 3 2 <br/>
5 4 8 7<br/>
8<br/>
7 5 3 2 5 105 45 10<br/>
2 4 0 5 6 9 75 84<br/>

**Sample Output**<br/>
YES<br/>
NO<br/>