## [2D Array - DS](https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays)
Given a 6 X 6 2D Array, <b>arr</b>:<br/>
<pre><code>1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
</code></pre><br/>
We define an hourglass in <b>A</b> to be a subset of values with indices falling in this pattern in <b>arr</b>'s graphical representation:<br/>
<pre><code>a b c
  d
e f g
</code></pre><br/>

There are <b>16</b> hourglasses in <b>arr</b>, and an hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in <b>arr</b>, then print the maximum hourglass sum.<br/>
For example, given the 2D array:<br/>
<pre><code>-9 -9 -9  1 1 1 
 0 -9  0  4 3 2
-9 -9 -9  1 2 3
 0  0  8  6 6 0
 0  0  0 -2 0 0
 0  0  1  2 4 0
</code></pre><br/>
We calculate the following 16 hourglass values:<br/>
<pre><code>-63, -34, -9, 12, 
-10, 0, 28, 23, 
-27, -11, -2, 10, 
9, 17, 25, 18
</code></pre><br/>
Our highest hourglass value is 28 from the hourglass:
<pre><code>0 4 3
  1
8 6 6
</code></pre><br/>


**Function Description**<br/>
Complete the function hourglassSum in the editor below. It should return an integer, the maximum hourglass sum in the array.<br/>
hourglassSum has the following parameter(s):

<ul><li>arr: an array of integers</li></ul>

**Input Format**<br/>
Each of the 6 lines of inputs <b>arr[i]</b> contains 6 space-separated integers <b>arr[i][j]</b>.<br/>

**Output Format** <br/>
Print the largest (maximum) hourglass sum found in <b>arr</b>.

**Sample Input**<br/>
<pre><code>1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
</code></pre><br>

**Sample Output**<br/>
19