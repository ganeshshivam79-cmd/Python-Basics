 CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    CONSTRAINT PK_Person PRIMARY KEY (ID,LastName)
);



 SELECT * FROM sales WHERE order_date >= NOW() - INTERVAL 1 DAY;
 it will helps to take data from last 24 hrs;
 
 

 SELECT GETDATE();
 --helps to get the current DATE
 
 
 CREATE TABLE Orders (
    OrderID int NOT NULL,
    OrderNumber int NOT NULL,
    PersonID int,
    PRIMARY KEY (OrderID),
    FOREIGN KEY (PersonID) REFERENCES Persons(PersonID)
);

foreign keys refers to priimary key of another table 

ALTER TABLE Persons ADD PRIMARY KEY (ID);
ALTER TABLE Persons
ADD CONSTRAINT PK_Person PRIMARY KEY (ID,LastName);


-- Scalar sun query  It returns 1 ROWS and 1 COLUMNS

select * from employee where salary > (select avg(salary) from employee);

select * from employee e1 join (select avg(salary) from employee) avg_sal on avg.salary< el.salary;

--- multiple row subquery
--  1 column many rows, many rows many columns
select * from employee where dept_name not in (select distinct dept_name from department);

--co related sub query
select * from employee e1 where salary> (select avg(salary) from employee e2 where e2.dept_name = e1.dept_name)

select dept_name from department_name where dept_name not exists  (select dept_name from employee);

SELECT DATENAME(year, '2017/08/25') AS DatePartString;
--2017
 SELECT DATEADD(DAY,1,'2017/08/25') ;
 -- Day, month, YEAR
 SELECT DATEDIFF(Day, '2011/08/25', '2017/08/25') AS DateDiff;
 --2192 days

SELECT MONTHNAME(date_column) AS month_name FROM table_name;
--Febrary

1. Keywords
1.CHECK
2.Default 
3.INSTR
4.EXISTS
5.  rows between 2 preceding  and current row 
6. Lead, LAG 
7

alter table customer add check (id>10);

ALTER TABLE Persons ADD CONSTRAINT df_City DEFAULT 'Sandnes' FOR City;

orderdate date default GetDate()


ALTER TABLE Persons ALTER City DROP DEFAULT;

ALTER TABLE Persons DROP CONSTRAINT CHK_PersonAge;


SELECT TO_CHAR(date_column, 'Month') AS month_name FROM table_name;


select A.ProductID from Sales A join sales B on A.proudctID=b.productID where A.ORDERDATE=DATE_SUB(B.ORDERDATE,INTERVAL 1 DAY) AND A.PRODUCT<B.PRODUCT;

