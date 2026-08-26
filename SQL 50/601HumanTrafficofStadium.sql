# Write your MySQL query statement below
select id,visit_date,people
from(
    select *,
    lag(people,1) over(order by id) as p1,
    lag(people,2) over(order by id) as p2,
    lead(people,1) over(order by id) as n1,
    lead(people,2) over(order by id) as n2
    from Stadium
) as x
where people>=100
and(
    (p1>=100 and p2>=100)or(p1>=100 and n1>=100)or(n1>=100 and n2>=100)
)order by visit_date;