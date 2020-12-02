# Write your MySQL query statement below
SELECT P.FirstName, P.LastName, A.City, A.State from Person as P left join Address as A on P.PersonId = A.PersonId;