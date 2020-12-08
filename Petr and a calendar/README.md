## Petr and a calendar
Petr wants to make a calendar for current month. For this purpose he draws a table in which columns correspond to weeks (a week is seven consequent days from Monday to Sunday), rows correspond to weekdays, and cells contain dates. For example, a calendar for January 2017 should look like on the picture:
<br/>

```
|   | 2 | 8  | 14 | 20 | 26 |
|   | 3 | 9  | 15 | 21 | 27 |
|   | 4 | 10 | 16 | 22 | 28 |
|   | 5 | 11 | 17 | 23 | 29 |
|   | 6 | 12 | 18 | 24 | 30 |
| 1 | 7 | 13 | 19 | 25 | 31 |
```
Petr wants to know how many columns his table should have given the month and the weekday of the first date of that month? Assume that the year is non-leap.

<b>Input Format</b><br/>You will be given a function with two integers m and d as arguments.<br/><br/>
<b>Constraints</b><br/>
1 <= m <= 12<br/>1 <= d <= 7<br/><br/>

<b>Output Format</b><br/>You need to return single integer: the number of columns the table should have..<br/><br/>
<b>Sample Input</b><br/>1<br/>7<br/><br/>
<b>Sample Output</b><br/>6
