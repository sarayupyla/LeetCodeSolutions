select email
from Person
group by email
having count(*)>1; #duplicates will be more than 1,so if count is greater than 1 then duplicate found