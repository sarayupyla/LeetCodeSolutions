select Register.contest_id,
round(count(distinct Register.user_id)*100.0/(select count(*) from Users),2) as percentage
from Register
group by Register.contest_id
order by percentage desc,Register.contest_id asc;
 