# Write your MySQL query statement below
select person_name
from (
    select person_name,weight,turn,
    sum(weight) over(order by turn)as run_wt
    from Queue
)as x
where run_wt<=1000
order by turn desc
limit 1;