select query_name,
round(avg(Queries.rating/Queries.position),2) as quality,
round(SUM(CASE when rating < 3 THEN 1 ELSE 0 END)* 100.0 / COUNT(*), 2) as poor_query_percentage
FROM Queries
group by query_name;