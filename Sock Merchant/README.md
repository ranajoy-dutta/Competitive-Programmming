## [Sock Merchant](https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup)
John works at a clothing store. He has a large pile of socks that he must pair by color for sale. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

For example, there are <b>n = 7</b> socks with colors <b>ar = [1, 2, 1, 2, 1, 3, 2]</b>. There is one pair of color <b>1</b> and one of color <b>2</b>. There are three odd socks left, one of each color. The number of pairs is <b>2</b>.<br/>

**Function Description**<br/>
Complete the sockMerchant function in the editor below. It must return an integer representing the number of matching pairs of socks that are available.<br/>
sockMerchant has the following parameter(s):
<ul><li>n: the number of socks in the pile</li>
<li>ar: the colors of each sock</li></ul>

**Input Format**<br/>
The first line contains an integer <i><b>n</i></b>, the number of socks represented in <i><b>ar</i></b>.<br/>.
The second line contains <i><b>n</i></b> space-separated integers describing the colors <i><b>ar[i]</i></b> of the socks in the pile.<br/>

**Output Format** <br/>
Return the total number of matching pairs of socks that John can sell.

**Sample Input**<br/>
9<br/>
10 20 20 10 10 30 50 10 20<br/>

**Sample Output**<br/>
3