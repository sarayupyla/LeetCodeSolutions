# Write your MySQL query statement below
select Department,Employee,salary 
from (
    select d.name as Department,e.name as Employee,e.salary,
    dense_rank() over(partition by e.departmentId order by e.salary DESC) as rnk
    from Employee as e
    join Department as d
    on e.departmentId=d.id
) as x
where rnk<=3;