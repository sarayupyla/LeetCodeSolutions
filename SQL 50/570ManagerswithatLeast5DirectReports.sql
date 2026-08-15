select m.name as name
from Employee as e
join Employee as m
on e.managerId =m.id
group by m.name,m.id
having count(*)>=5;