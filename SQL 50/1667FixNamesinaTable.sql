select user_id,CONCAT(upper(left(name,1)),lower(substring(name,2))) as name
from Users
order by user_id;