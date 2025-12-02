

last 5 records fetching
select * from student s1 where 5>=(select count(distinct GPA) from student s2 where s1.GPA>=s2.GPA) order by GPA desc;

First 5 records fetching
select * from student s1 where 5>=(select count(distinct GPA) from student s2 where s1.GPA<=s2.GPA) order by GPA desc;



Write an SQL query to fetch the list of Students with the same GPA.
select * from student s1 join student s2 on s1.GPA=s2.GPA where s1.student_name!=s2.student_name;


SELECT
  Orders.Items AS Items, Split.value as splitValue FROM [dbo].[Orders] AS 
CROSS APPLY STRING_SPLIT(Orders.Items, ',') as Split;

1. Join -- self join
2.Auto increment, DEFAULT, CHECK
3.Primary key, foreign key CONSTRAINTS
4.DATEADD, DATENAME, DATEDIFF
5.count, SUM, MIN, MAX -- Aggregate function
6.offset, limit, Top 3, COALESCE
7.charindex, Reverse


cast(student_id) as int
CAST(REPLACE(salary, ',', '') AS INT) BETWEEN 50000 AND 60000;
SELECT CHARINDEX('at', 'database');
SELECT CHARINDEX('a', 'banana', 3);
-- returns 4 searching starts at position 3
select reverse("data");
SELECT SUBSTRING('Sidekick', 1, 4)

CREATE TABLE student (
    student_id INT PRIMARY KEY,
    name VARCHAR(255),
    Age INT AUTO_INCREMENT,
    class INT DEFAULT 7
);


SELECT DATENAME(year, '2017/08/25') AS DatePartString;
--2017
 SELECT DATEADD(DAY,1,'2017/08/25') ;
 -- Day, month, YEAR
 SELECT DATEDIFF(Day, '2011/08/25', '2017/08/25') AS DateDiff;
 --2192 days

SELECT MONTHNAME(date_column) AS month_name FROM table_name;
--Febrary

---- --------------------------------------------------------------------------
------------------------------Logic questions-------------------------------

 SELECT * FROM sales WHERE order_date >= NOW() - INTERVAL 1 DAY;
 it will helps to take data from last 24 hrs;
 
 
 
 -- Scalar sun query  It returns 1 ROWS and 1 COLUMNS

select * from employee where salary > (select avg(salary) from employee);

select * from employee e1 join (select avg(salary) from employee) avg_sal on avg.salary< el.salary;

--- multiple row subquery
--  1 column many rows, many rows many columns
select * from employee where dept_name not in (select distinct dept_name from department);

--co related sub query
select * from employee e1 where salary> (select avg(salary) from employee e2 where e2.dept_name = e1.dept_name)
select dept_name from department_name where dept_name not exists  (select dept_name from employee);


---- --------------------------------------------------------------------------
------------------------------Logic questions-------------------------------


SELECT
    CASE
        WHEN salary > 50000 THEN 'High Earner'
        WHEN salary BETWEEN 30000 AND 50000 THEN 'Middle Earner'
        ELSE 'Low Earner'
    END AS IncomeGroup
FROM employees;


---- --------------------------------------------------------------------------
------------------------------Logic questions-------------------------------


SELECT
    SUM(CASE
        WHEN region = 'North' THEN sales
        ELSE 0
    END) AS NorthSales,
    SUM(CASE
        WHEN region = 'South' THEN sales
        ELSE 0
    END) AS SouthSales
FROM sales_data;


SELECT
    CONCAT('Hello, ', CASE
        WHEN country = 'USA' THEN 'American'
        WHEN country = 'Canada' THEN 'Canadian'
        ELSE 'International'
    END, ' customer!') AS Greeting
FROM customers;


CREATE VIEW customer_info AS
SELECT customer_id AS id, name AS customer_name, email, phone
FROM customers;

ALTER TABLE employees MODIFY job_title VARCHAR2(50);

SELECT Orders.OrderID, Split.value
FROM Orders CROSS APPLY STRING_SPLIT(Orders.Items, ',') as Split;


WITH temporaryTable(averageValue) as
    (SELECT avg(Salary)
    from Employee)
        SELECT EmployeeID,Name, Salary 
        FROM Employee, temporaryTable 
        WHERE Employee.Salary > temporaryTable.averageValue;
		
		
select challenge_id, h_id, h_name, score, dense_rank() over ( partition by challenge_id order by score desc ) as "rank", from hacker;


UPDATE students SET students_date = DATE_ADD(students_date, INTERVAL 1 YEAR) WHERE YEAR(students_date) = 2018;

SELECT SUBJECT, AVG(MARKS) OVER (PARTITION BY SUBJECT) AS "AVERAGE MARKS" FROM STDMARKS;


WITH subject_averages AS (
  SELECT SUBJECT, AVG(MARKS) as Average FROM students_table GROUP BY SUBJECT
)
SELECT *, RANK() OVER (ORDER BY subject_averages.Average DESC) as Rank
FROM subject_averages ORDER BY subject_averages.Average DESC;

SELECT *
FROM your_table
WHERE 
    (MONTH(date_column) = 3 AND DAY(date_column) >= 3) 
    OR (MONTH(date_column) = 4 AND DAY(date_column) <= 10);
	
SELECT * FROM your_table WHERE  DATE_FORMAT(date_column, '%m-%d') BETWEEN '03-03' AND '04-10';

-----------------------------------------------------------------------------------------------------------------
SELECT student_id, first_name, last_name, SUM(marks) as total_marks,
  RANK() OVER (ORDER BY SUM(marks) DESC) as rank
FROM students GROUP BY student_id, first_name, last_name;   --- You cant use this in right way


SELECT student_id, first_name, last_name, total_marks,
  RANK() OVER (ORDER BY total_marks DESC) as rank from (select student_id, first_name, last_name, sum(marks) as total_marks from students_table
  group by student_id, first_name, last_name) as subquery ORDER BY total_marks DESC;
 -----------------------------------------------------------------------------------------------------------------



select A.ProductID from Sales A join sales B on A.proudctID=b.productID where A.ORDERDATE=DATE_SUB(B.ORDERDATE,INTERVAL 1 DAY) AND A.PRODUCT<B.PRODUCT;


SELECT student_id, class, score, RANK() OVER (PARTITION BY class ORDER BY score DESC) as rank
FROM student_scores;


SELECT student_id, first_name, last_name, section, marks, ROW_NUMBER() OVER (PARTITION BY section ORDER BY marks DESC) AS rank
FROM students;

SELECT  City AS CustomerCity, CustomerName, amount, COUNT(*) OVER (PARTITION BY city) AS total_orders
FROM [SalesLT].[Orders];


ROW_NUMBER, RANK(), COUNT(*), Min, Max


ALTER TABLE sales_data
ADD sales_site VARCHAR(3);

UPDATE sales_data
SET sales_site = CASE
    WHEN salestotal > 100 THEN 'Yes'
    ELSE 'No'
END;

SELECT 
  CustomerID, 
  OrderDate, 
  OrderAmount,
  MIN(OrderAmount) OVER (PARTITION BY CustomerID) AS MinOrderAmount,
  MAX(OrderAmount) OVER (PARTITION BY CustomerID) AS MaxOrderAmount
FROM 
  SalesOrders
ORDER BY 
  CustomerID, OrderDate;

SELECT 
  CustomerID, 
  OrderDate, 
  OrderAmount,
  MIN(OrderAmount) OVER (PARTITION BY CustomerID) AS MinOrderAmount,
  MAX(OrderAmount) OVER (PARTITION BY CustomerID) AS MaxOrderAmount,
  ROW_NUMBER() OVER (PARTITION BY CustomerID ORDER BY OrderDate) AS RowNumber
FROM 
  SalesOrders
ORDER BY 
  CustomerID, OrderDate;
