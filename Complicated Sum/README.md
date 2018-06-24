## Complicated Sum
> **Considering the code below, Calculate the final value of sum if n is provided as input.**
<br/>
M = 1000000007<br/>
long long int sum = 0;<br/>
for (long long int i = 1;i<=n;i++) {<br/>
    for (long long int j = i;j<=n;j++) {<br/>
        long long int iTemp = i%M;<br/>
        long long int jTemp = j%M;<br/>
        sum = (sum + (iTemp*jTemp) % M ) % M;    }}<br/>

**Input**<br/>
The first Line of input consist of T - the number of test cases. T lines follows - each consisting of single integer n<br/>

**Output** <br/>
Output in T lines the answer to each test case. 
