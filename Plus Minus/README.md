## Plus Minus
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to 10^-4 are acceptable.

**Example**<br/>
arr = [1,1,0,-1,-1]<br/>
There are n=5 elements, two positive, two negative and one zero. Their ratios are 
<br/>
![\Large \frac{2}{5}](https://latex.codecogs.com/svg.image?\frac{2}{5}=0.400000), ![\Large \frac{2}{5}](https://latex.codecogs.com/svg.image?\frac{2}{5}=0.400000) and ![\Large \frac{1}{5}](https://latex.codecogs.com/svg.image?\frac{1}{5}=0.200000).

Results are printed as:

    0.400000
    0.400000
    0.200000

**Function Description** <br/>
Complete the plusMinus function in the editor below.

plusMinus has the following parameter(s):
 - int arr[n]: an array of integers

**Print**<br/>
Print the ratios of positive, negative and zero values in the array. Each value should be printed on a separate line with 6 digits after the decimal. The function should not return a value.

**Input Format**<br/>
The first line contains an integer, n, the size of the array.
The second line contains n space-separated integers that describe arr[n].

**Constraints**<br/>
![0<n<=100](https://latex.codecogs.com/svg.image?0<n\leq100) <br/>
![-100<arr[i]<=100](https://latex.codecogs.com/svg.image?-100\leq&space;arr[i]\leq100)

**Output Format**<br/>
Print the following 3 lines, each to 6 decimals:

 - proportion of positive values
 - proportion of negative values
 - proportion of zeros

**Sample Input**<br/>

    STDIN           Function
    -----           --------
    6               arr[] size n = 6
    -4 3 -9 0 4 1   arr = [-4, 3, -9, 0, 4, 1]

**Sample Output**<br/>

    0.500000
    0.333333
    0.166667
    
**Explanation**<br/>
There are 3 positive numbers, 2 negative numbers, and 1 zero in the array.
The proportions of occurrence are positive: ![\frac{3}{6}=0.500000](https://latex.codecogs.com/svg.image?\frac{3}{6}=0.500000), negative: ![\frac{2}{6}=0.333333](https://latex.codecogs.com/svg.image?\frac{2}{6}=0.333333) and zeros: ![\frac{1}{6}=0.166667](https://latex.codecogs.com/svg.image?\frac{1}{6}=0.166667).
