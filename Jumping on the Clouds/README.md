## [Jumping on the Clouds](https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup)
Emma is playing a new mobile game that starts with consecutively numbered clouds. Some of the clouds are thunderheads and others are cumulus. She can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus <b>1</b> or <b>2</b>. She must avoid the thunderheads. Determine the minimum number of jumps it will take Emma to jump from her starting postion to the last cloud. It is always possible to win the game.
<br>
For each game, Emma will get an array of clouds numbered <b>0</b> if they are safe or <b>1</b> if they must be avoided. For example, <b>c=[0,1,0,0,0,1,0]</b> indexed from <b>0 . . . 6</b>. The number on each cloud is its index in the list so she must avoid the clouds at indexes <b>1</b> and <b>5</b>. She could follow the following two paths: <b>0 -> 2 -> 4 -> 6</b> or <b>0 -> 2 -> 3 -> 4 -> 6</b>. The first path takes <b>3</b> jumps while the second takes <b>4</b>.

**Function Description**<br/>
Complete the jumpingOnClouds function in the editor below. It should return the minimum number of jumps required, as an integer.
<br>
jumpingOnClouds has the following parameter(s):
<br>
<ul><li>c: an array of binary integers</li></ul>

**Input Format**<br/>
The first line contains an integer <b><i>n</i></b>, the total number of clouds. The second line contains <b><i>n</i></b> space-separated binary integers describing clouds <b><i>c[i]</i></b> where <b><i>0 <= i <= n</i></b>.<br/>

**Output Format** <br/>
Print the minimum number of jumps needed to win the game.<br>


**Sample Input**<br/>
7<br/>
0 0 1 0 0 1 0<br/>

**Sample Output**<br/>
4
