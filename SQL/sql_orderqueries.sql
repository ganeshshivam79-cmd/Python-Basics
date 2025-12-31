-- Example: Count employees per department with salary > 30000, order by count
SELECT dept_id, COUNT(*) AS emp_count
FROM employees
WHERE salary > 30000       -- filter rows first
GROUP BY dept_id            -- then group
ORDER BY emp_count DESC;    -- finally sort


-- Example: Count employees per department and show only departments with > 5 employees
SELECT dept_id, COUNT(*) AS emp_count
FROM employees
GROUP BY dept_id            -- group first
HAVING COUNT(*) > 5         -- filter groups after aggregation
ORDER BY emp_count DESC;    -- sort results


-- Example: Top 3 departments with highest employees, skip the first 2
SELECT dept_id, COUNT(*) AS emp_count
FROM employees
GROUP BY dept_id
HAVING COUNT(*) > 2         -- filter aggregated groups
ORDER BY emp_count DESC     -- sort by count
LIMIT 3 OFFSET 2;           -- pagination: skip 2 rows, take next 3
