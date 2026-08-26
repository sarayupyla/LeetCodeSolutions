CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
    SELECT max(salary)  -- it doesn't return more than one row if both have same values
    FROM (
        SELECT salary,
               DENSE_RANK() OVER(ORDER BY salary DESC) AS rnk
        FROM Employee
    ) AS x
    WHERE rnk = n
  );
END