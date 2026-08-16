select 'High Salary' as  category,sum(if(income>50000,1,0)) as accounts_count
from Accounts
UNION ALL
select 'Low Salary',sum(if(income<20000 ,1,0)) as accounts_count
from Accounts
UNION ALL
select 'Average Salary',sum(if(income between 20000 and 50000,1,0)) as accounts_count
from Accounts;