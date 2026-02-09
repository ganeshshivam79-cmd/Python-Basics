1.Fetch data of 21 to 30
SELECT * FROM customers ORDER BY customer_id OFFSET 20 ROWS FETCH NEXT 10 ROWS ONLY;f
--fetch 21 to 30 data only

2.To fetch only even-ranked students based on their total marks in descending order, you can use ROW_NUMBER() or RANK() with a CASE or MOD filter.

WITH ranked_students AS (
  SELECT student_id, student_name, total_marks,
         ROW_NUMBER() OVER (ORDER BY total_marks DESC) AS rank_num
  FROM students
)
SELECT student_id, student_name, total_marks, rank_num
FROM ranked_students
WHERE MOD(rank_num, 2) = 0;  -- Even ranks only


select * from ( select students_id, row_number() over (order by total_marks  desc) as ranks  from school) t where 
mod(t.ranks,2)=0;


SELECT customer_id
FROM customers
WHERE YEAR(order_date) = 2023 GROUP BY customer_id HAVING COUNT(DISTINCT MONTH(order_date)) = 12;


select customer_id, sum(order_amount)/(select sum(order_amount) from customers) from customers
group by customer_id 

SELECT
  product_id,
  SUM(order_amount) AS product_revenue,
  100.0 * SUM(order_amount) / NULLIF(SUM(SUM(order_amount)) OVER (), 0) AS revenue_pct
FROM customers
GROUP BY product_id
ORDER BY revenue_pct DESC;


WITH ranked_products AS (
    SELECT
        product_id,
        SUM(revenue) OVER (
            ORDER BY revenue DESC
            ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
        ) * 1.0 / SUM(revenue) OVER () AS cumulative_pct
    FROM product_revenue
)
SELECT *
FROM ranked_products
WHERE cumulative_pct <= 0.8;



WITH yearly AS (
  SELECT
    YEAR(order_date) AS order_date_year,
    SUM(revenue) AS year_revenue
  FROM customers
  GROUP BY YEAR(order_date)
)
SELECT
  order_date_year,
  year_revenue,
  year_revenue - LAG(year_revenue) OVER (ORDER BY order_date_year) AS year_growth
FROM yearly
ORDER BY [year];



with below_revenue as ( select customer, ntile(10) over ( partition by customer_id order by total_amount desc ) as revenue from customer)
select customer_id, revenue from below_revenue where revenue=10;


