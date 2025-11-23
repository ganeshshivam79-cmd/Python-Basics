DATEDIFF(MONTH, '2024-01-01', GETDATE());
it will difference the DATE 

SELECT DATEADD(MONTH, -2, GETDATE());
it will subtract two months date 

DATEDIFF(QUARTER, 0, GETDATE())
 0 is 1900 it gives all qauter YEAR
 

MONTH(order_date) = MONTH(GETDATE()) -- to get current month DATA 

DATEADD(QUARTER, -1, DATEADD(QUARTER, DATEDIFF(QUARTER, 0, GETDATE()), 0))

LEAD(salary) OVER (ORDER BY employee_id) AS next_salary



 select ordername, order id from orders l left join orders r on l.ordername=r.ordername where r.orderdate=DateADD(date,-6, GETDATe()) 
 and r.order_id is NULL;
 
 ###################################################################################################
 --November 23 2025
| Function          | Output       |
| ----------------- | ------------ |
| DATENAME(year, date)    | **2025**     |
| DATENAME(month, date)   | **November** |
| DATENAME(day,date)     | **23**       |
| DATENAME(weekday,date) | **Sunday**   |
| DATENAME(week, date)    | **48**       |
| DATENAME(quarter, date) | **4**        |



DATEPART(year, date)         -- 2025
DATEPART(month, date)        -- 1 to 12
DATEPART(day, date)          -- 1 to 31
DATEPART(weekday, date)      -- 1 to 7
DATEPART(week, date)         -- week number
DATEPART(quarter, date)      -- Q1 to Q4
DATEPART(dayofyear, date)    -- 1 to 365
DATEPART(hour, date)
DATEPART(minute, date)
DATEPART(second, date)
DATEPART(millisecond, date)


YEAR(date)
MONTH(date)
DAY(date)

All are integers above one give


DATEADD(day, 5, date)
DATEADD(month, -1, date)
DATEADD(year, 2, date)
DATEADD(week, 3, date)
DATEADD(hour, 10, date)



DATEDIFF(day, date1, date2)
DATEDIFF(month, date1, date2)
DATEDIFF(year, date1, date2)
DATEDIFF(week, date1, date2)


All are integers
################################################################