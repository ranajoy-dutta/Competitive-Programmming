## [Repeated String](https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup)
Lilah has a string, <b>s</b>, of lowercase English letters that she repeated infinitely many times.<br/>
Given an integer, <b>n</b>, find and print the number of letter a's in the first  letters of Lilah's infinite string.<br/>
For example, if the string <b>s = 'abcac'</b> and <b>n = 10</b>, the substring we consider is <b>abcacabcac</b>, the first <b>10</b> characters of her infinite string. There are <b>4</b> occurrences of a in the substring.<br/>

**Function Description**<br/>
Complete the repeatedString function in the editor below. It should return an integer representing the number of occurrences of a in the prefix of length  in the infinitely repeating string.<br/>
repeatedString has the following parameter(s):
<ul><li>s: a string to repeat</li>
<li>n: the number of characters to consider</li></ul><br/>

**Input Format**<br/>
The first line contains a single string, <i><b>s</i></b>.<br/>
The second line contains an integer, <i><b>n</i></b>.<br/>

**Output Format** <br/>
Print a single integer denoting the number of letter a's in the first <b>n</b> letters of the infinite string created by repeating <b>s</b> infinitely many times.

**Sample Input**<br/>
aba<br/>
10<br/>

**Sample Output**<br/>
7