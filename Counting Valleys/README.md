## Counting Valleys
Gary is an avid hiker. He tracks his hikes meticulously, paying close attention to small details like topography. During his last hike he took exactly <ul>
<li>A <em>mountain</em> is a sequence of consecutive steps <em>above</em> sea level, starting with a step <em>up</em> from sea level and ending with a step <em>down</em> to sea level.  </li>
<li>A <em>valley</em> is a sequence of consecutive steps <em>below</em> sea level, starting with a step <em>down</em> from sea level and ending with a step <em>up</em> to sea level.</li>
</ul><p>Given Gary's sequence of <em>up</em> and <em>down</em> steps during his last hike, find and print the number of <em>valleys</em> he walked through. </p> <p>For example, if Gary's path is <b><i>s=[DDUUUUDD]</i></b>, he first enters a valley <b>2</b> units deep. Then he climbs out an up onto a mountain <b>2</b> units high. Finally, he returns to sea level and ends his hike.  </p><b>Function Description</b><p>Complete the <em>countingValleys</em> function in the editor below.  It must return an integer that denotes the number of valleys Gary traversed.  </p><p>countingValleys has the following parameter(s):  </p><ul>
<li><em>n</em>: the number of steps Gary takes  </li>
<li><em>s</em>: a string describing his path  </li>
</ul>

**Input Format**<br/>
The first line contains an integer n, the number of steps in Gary's hike.<br>
The second line contains a single string s, of n characters that describe his path.<br/>

**Output Format** <br/>
Print a single integer that denotes the number of valleys Gary walked through during his hike.<br>


**Sample Input**<br/>
8<br/>
UDDDUDUU<br/>

**Sample Output**<br/>
1
