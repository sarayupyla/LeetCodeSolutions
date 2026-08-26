# Write your MySQL query statement below
select Department,Employee,salary 
from (
    select d.name as Department,e.name as Employee,e.salary,
    max(e.salary) over(partition by e.departmentId) as max_salary
    from Employee  as e
    join Department as d
    on e.departmentId=d.id
) as x
where salary=max_salary;