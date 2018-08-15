## String Formatting

> **Given an integer, n, print the following values for each integer i from 1 to n:
1. Decimal
2. Octal
3. Hexadecimal (capitalized)
4. Binary
5. The four values must be printed on a single line in the order specified above for each  from  to . Each value should be space-padded to match the width of the binary value of n.<br/>**

**Input Format**<br/>
A single integer denoting n.<br/>

**Output Format** <br/>
Print  lines where each line i (in the range 1<=i<=n) contains the respective decimal, octal, capitalized hexadecimal, and binary values of i. Each printed value must be formatted to the width of the binary value of n.<br/>

**Sample Input**<br/>
17<br>

**Sample Output**<br/>
    1     1     1     1<br/>
    2     2     2    10<br/>
    3     3     3    11<br/>
    4     4     4   100<br/>
    5     5     5   101<br/>
    6     6     6   110<br/>
    7     7     7   111<br/>
    8    10     8  1000<br/>
    9    11     9  1001<br/>
   10    12     A  1010<br/>
   11    13     B  1011<br/>
   12    14     C  1100<br/>
   13    15     D  1101<br/>
   14    16     E  1110<br/>
   15    17     F  1111<br/>
   16    20    10 10000<br/>
   17    21    11 10001  