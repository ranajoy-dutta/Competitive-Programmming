## Combine Two Tables
**Write a SQL query for a report that provides the following information for each person in the Person table, regardless if there is an address for each of those people:<br/>**
```
FirstName, LastName, City, State
```
<br/>
**Table:** Person<br/>
```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| PersonId    | int     |
| FirstName   | varchar |
| LastName    | varchar |
+-------------+---------+
PersonId is the primary key column for this table.
```

**Table:** Address<br/>
```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| AddressId   | int     |
| PersonId    | int     |
| City        | varchar |
| State       | varchar |
+-------------+---------+
AddressId is the primary key column for this table.
```
