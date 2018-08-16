## Merge The Tools
Consider the following:
A string, s, of length n.
An integer, k, where k is a factor of n.
We can split s into n/k subsegments where each subsegment, t(i), consists of a contiguous block of k characters in s.
Then, use each t(i) to create string u(i) such that:
The characters in u(i) are a subsequence of the characters in t(i).
Any repeat occurrence of a character is removed from the string such that each character in u(i) occurs exactly once. 
In other words, if the character at some index j in t(i) occurs at a previous index < j in t(i), then do not include the 
character in string u(i).
Given s and k, print n/k lines where each line i denotes string u(i).
Input Format
The first line contains a single string denoting s. 
The second line contains an integer, k, denoting the length of each subsegment.
Output Format
Print n/k lines where each line i contains string u(i).
Sample Input
AABCAAADA
3   
Sample Output
AB
CA
AD
