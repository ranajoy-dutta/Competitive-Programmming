Considering the code below, Calculate the final value of sum if n is provided as input.

M = 1000000007
long long int sum = 0;
for (long long int i = 1;i<=n;i++) {
    for (long long int j = i;j<=n;j++) {
        long long int iTemp = i%M;
        long long int jTemp = j%M;
        sum = (sum + (iTemp*jTemp) % M ) % M;    }}

Input ::  
The first Line of input consist of T - the number of test cases. T lines follows - each consisting of single integer n

Output :: 
Output in T lines the answer to each test case. 
