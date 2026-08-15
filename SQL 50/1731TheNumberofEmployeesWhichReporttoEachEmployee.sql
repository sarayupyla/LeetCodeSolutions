select t2.employee_id,t2.name,count(*) as reports_count,round(avg(t1.age),0) as average_age
from Employees as t1
join Employees as t2
on t1.reports_to=t2.employee_id
group by t1.reports_to
order by t2. employee_id;