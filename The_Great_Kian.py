"""The great Kian is looking for a smart prime minister. He's looking for a guy who can solve the OLP (Old Legendary Problem). 
OLP is an old problem (obviously) that no one was able to solve it yet (like P=NP).
But still, you want to be the prime minister really bad. So here's the problem:

Given the sequence a1, a2, ..., an find the three values a1 + a4 + a7 + ..., a2 + a5 + a8 + ... and a3 + a6 + a9 + ... (these summations go on while the indexes are valid).

Input
The first line of input contains a single integer n (1 ≤ n ≤ 105).
The second line contains n integers a1, a2, ..., an separated by space (1 ≤ ai ≤ 109).

Output
Print three values in one line (the answers).

|  SAMPLE INPUT           |             SAMPLE OUTPUT  |
|  5                      |             5 7 3          |
|  1 2 3 4 5              |                            | """


n = int(input().strip())
a = [int(x) for x in input().strip().split()]         
print("{} {} {}".format(sum(a[::3]),sum(a[1::3]),sum(a[2::3])))
