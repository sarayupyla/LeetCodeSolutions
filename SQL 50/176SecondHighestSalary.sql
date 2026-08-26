/*SELECT MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary < (SELECT MAX(salary) FROM Employee);*/

select(
    select salary from(
        select salary,
        dense_rank() over(order by salary desc) as rnk
        from Employee
    )as x
    where rnk=2
)as SecondHighestSalary ;