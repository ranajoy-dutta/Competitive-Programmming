# Write your MySQL query statement below
SELECT IFNULL(
    (SELECT distinct Salary
     FROM Employee 
     ORDER BY Salary desc limit 1,1),NULL) 
     As SecondHighestSalary;
