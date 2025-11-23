1.Want to see only products that had at least one date gap?

WITH sales_with_gap AS (
  SELECT 
      product_id,
      sale_date,
      LAG(sale_date) OVER (PARTITION BY product_id ORDER BY sale_date) AS prev_sale_date
  FROM sales
)
SELECT DISTINCT product_id
FROM sales_with_gap
WHERE DATEDIFF(day, prev_sale_date, sale_date) > 1;



2.second rank in each department 

WITH second_rank AS (
    SELECT 
        department_id, 
        salary,
        RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS ranks
    FROM school
)
SELECT *
FROM second_rank
WHERE ranks = 2;


3. This is one the best question
Find sales id which are null for past three months 

SELECT p.product_id, p.product_name
FROM products p
LEFT JOIN sales s ON 
    p.product_id = s.product_id AND
    s.sale_date >= DATEADD(QUARTER, -1, 
	)), 0)) AND
    s.sale_date <  DATEADD(QUARTER, DATEDIFF(QUARTER, 0, GETDATE()), 0)
WHERE s.sale_id IS NULL;


SELECT p.product_id, p.product_name
FROM products p
LEFT JOIN sales s 
    ON p.product_id = s.product_id
    AND s.sale_date >= DATEADD(MONTH, -3, GETDATE())
WHERE s.sale_id IS NULL;

4. Find back to  know purchase of customers within 1 month meaning consecutive months of purchase

WITH customer_months AS (
  SELECT 
    customer_id, 
    order_date,
    DATEDIFF(
      MONTH, 
      LAG(order_date) OVER (PARTITION BY customer_id ORDER BY order_date), 
      order_date
    ) AS months_diff
  FROM orders
)
SELECT *
FROM customer_months
WHERE months_diff = 1;

5.
SELECT 
    employee_id,
    salary,
    NTILE(4) OVER (ORDER BY salary DESC) AS salary_quartile
FROM employees;

6.compare weekly average
SELECT
    DATEPART(YEAR, order_date) AS order_year,
    DATEPART(WEEK, order_date) AS week_number,
    AVG(sales_amount) AS weekly_avg_sales,
    AVG(sales_amount) - LAG(AVG(sales_amount)) OVER (PARTITION BY DATEPART(YEAR, order_date) 
                                                     ORDER BY DATEPART(WEEK, order_date)) AS diff_from_prev_week
FROM sales
GROUP BY
    DATEPART(YEAR, order_date),
    DATEPART(WEEK, order_date)
ORDER BY
    order_year,
    week_number;

7.Limit comes first and offset second

SELECT * FROM employees
ORDER BY salary DESC  LIMIT 5 OFFSET 10;  -- Skip first 10 rows, return next 5 rows

SELECT * FROM employees ORDER BY salary DESC
OFFSET 10 ROWS FETCH NEXT 5 ROWS ONLY;

