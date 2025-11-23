SQL most advanced question

1.

WITH product_sales AS (
    SELECT 
        product_category,
        product_id,
        SUM(quantity) AS total_sales,
        ROW_NUMBER() OVER (PARTITION BY product_category ORDER BY SUM(quantity) DESC) AS rn
    FROM department
    GROUP BY product_category, product_id
)
SELECT product_category, product_id, total_sales
FROM product_sales
WHERE rn = 1;

we used sum(quantity) so group by NEEDED, so based on sum it will calculate 



2.
WITH product_revenue AS (
    SELECT 
        product_id,
        SUM(price * quantity) AS revenue
    FROM orders
    GROUP BY product_id
),
ranked_revenue AS (
    SELECT 
        product_id,
        revenue,
        SUM(revenue) OVER (ORDER BY revenue DESC) AS cumulative_revenue,
        SUM(revenue) OVER () AS total_revenue
    FROM product_revenue
)
SELECT 
    product_id,
    revenue,
    ROUND((cumulative_revenue * 100.0) / total_revenue, 2) AS cumulative_percentage
FROM ranked_revenue
WHERE (cumulative_revenue * 1.0) / total_revenue <= 0.80;

calculate sum first for each product id and cumulative sum and then comparte data 




[100,200, 300, 400, 500]
Position = (5 - 1) × 0.9 = 4 × 0.9 = **3.6**
Percentile_90 = 400 + 0.6 × (500 - 400)
              = 400 + 60
              = 460
  


3. percentile greater than 90 percent 

-- Step 1: Calculate 90th percentile per customer
WITH percentile_table AS (
    SELECT
        customer_id,
        PERCENTILE_CONT(0.9) WITHIN GROUP (ORDER BY purchase_amount) 
            OVER (PARTITION BY customer_id) AS p90,
        purchase_id,
        purchase_amount
    FROM purchases
)
-- Step 2: Filter those who exceed their 90th percentile
SELECT customer_id, purchase_id, purchase_amount, p90
FROM percentile_table
WHERE purchase_amount > p90;
