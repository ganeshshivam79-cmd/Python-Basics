-- Non-correlated subquery in WHERE
SELECT name
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);


B. Correlated Subquery (Depends on Outer Query)
Inner query references outer query columns.
Runs once per outer row.

SELECT e1.name, e1.salary
FROM employees e1
WHERE e1.salary > (
    SELECT AVG(e2.salary)
    FROM employees e2
    WHERE e2.dept_id = e1.dept_id
);


C. Subquery in FROM Clause (Derived Table / Inline View)
Acts like a temporary table.
Must give an alias for outer query to reference it.

SELECT dept_id, MAX(salary) AS max_salary
FROM (
    SELECT dept_id, salary
    FROM employees
    WHERE salary > 30000
) AS high_salary_emps
GROUP BY dept_id;

D. Subquery in SELECT Clause
Returns a single value per row.
SELECT name,
       (SELECT MAX(salary) FROM employees) AS max_salary
FROM employees;


E. EXISTS / IN Subquery
Returns TRUE/FALSE or matches values.
SELECT name
FROM employees
WHERE dept_id IN (
    SELECT dept_id
    FROM department
    WHERE location = 'Mumbai'
);
