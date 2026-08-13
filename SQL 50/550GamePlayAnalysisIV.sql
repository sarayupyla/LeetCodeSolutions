select round( count(*)/(select count(distinct player_id) from Activity),2) as fraction
from Activity
where (player_id,event_date) in (
    select player_id,DATE_ADD(min(event_date),INTERVAL 1 DAY)
    from Activity
    group by player_id
);