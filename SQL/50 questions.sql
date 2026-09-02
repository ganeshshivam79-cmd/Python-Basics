

---------------------------------------------------
first time order of customer

WITH cte1 AS (
    SELECT
        order_id,
        order_date,
        customer_id,
        quantity,
        price,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id
            ORDER BY order_date
        ) AS rn
    FROM Orders
)
SELECT
    SUM(quantity * price) AS new_customer_revenue
FROM cte1
WHERE rn = 1;

--------------------------------------------------------
Pareto principle

WITH cte1 AS (
    SELECT
        customer_id,
        SUM(product * price) AS revenue
    FROM customer
    GROUP BY customer_id
),
cte2 AS (
    SELECT
        SUM(revenue) AS total_revenue
    FROM cte1
),
cte3 AS (
    SELECT
        s.customer_id,
        s.revenue,
        s1.total_revenue,
        SUM(s.revenue) OVER (
            ORDER BY s.revenue DESC
        ) AS running_revenue
    FROM cte1 s
    CROSS JOIN cte2 s1
)
SELECT
    customer_id,
    revenue,
    running_revenue,
    total_revenue,
    (running_revenue * 100.0) / total_revenue AS cumulative_pct
FROM cte3
WHERE (running_revenue * 100.0) / total_revenue <= 80
ORDER BY revenue DESC;

-------------------------------------------

SELECT 
    SUBSTRING(c.val, n.n, 1) AS data
FROM customer c
CROSS JOIN (
    SELECT TOP 100
        ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS n
    FROM sys.objects
) n
WHERE n.n <= LEN(c.val);
--------------------------------------------------------------------------

ntile split data into each subgroup okay

WITH customer_history AS (
    SELECT
        customer_id,
        order_id,
        total_amount,
        PERCENTILE_CONT(0.90)
            WITHIN GROUP (ORDER BY total_amount)
            OVER (
                PARTITION BY customer_id
                ORDER BY order_date
                ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING
            ) AS historical_90th
    FROM Orders
)
SELECT
    customer_id,
    order_id,
    total_amount
FROM customer_history
WHERE total_amount > historical_90th;
-------------------------------------------------------------------
Position:   1    2    3
Value:     100  200  300
(n - 1) × percentile + 1
(3 - 1) × 0.90 + 1
2 × 0.90 + 1
1.8 + 1
= 2.8

200 + 80% of (300 - 200)
200 + 80
= 280