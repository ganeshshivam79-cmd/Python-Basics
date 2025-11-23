Performance_Date >= DATEFROMPARTS(YEAR(GETDATE()), 1, 1)

Performance_Date >= DATEADD(MONTH, -6, GETDATE())  

DATEDIFF(DAY, HireDate, GETDATE()): --- difference of date whther based on DAY, MONTH , YEAR

SELECT 
    Fund_Name,
    (MAX(NAV) - MIN(NAV)) / NULLIF(MIN(NAV), 0) AS YTD_Return
FROM 
    Fund_Performance
GROUP BY 
    Fund_Name;
 --Using NULLIF you can avoid divisonerror
 
 
#############################################################################################################################

 CREATE INDEX index_name
ON table_name (column_name1, column_name2, ...);


A clustered index is a type of database index that organizes the physical storage of data in a table based on the values in the indexed column(s). It determines the order in which rows are stored on disk, making it highly efficient for range-based queries and lookups on the indexed column(s).

#############################################################################################################################

 SELECT ISNULL(NULL, 'No Value');
IFNULL(Column1, 'Default Value') AS Column1_Default,
-- Returns 'No Value' since the first argument is NULL.
-- SQL Server
SELECT ISNULL(NULL, 'hello')            -- returns 'hello'
SELECT COALESCE(NULL, NULL, 'world')    -- returns 'world'


 coalesce
 COALESCE(Column2, Column3, 'Fallback Value') AS Column2_Or_Column3_Or_Fallback
 returns first non null values
 meaning colesce return one non null vlues from colum order by going, if nit it returns default value

 SELECT NULLIF(10, 10);
-- Returns NULL because the two expressions are equal.

SELECT IFNULL(NULL, 'Default Value');
-- Returns 'Default Value' as the first argument is NULL.


OFFSET -- skip the rows 
sign(id) -- positive or negative
mod(10,3) -- remainder
FETCH NEXT 5 rows only; -- fetch additional 5 rows 


Under the 

PARTiTION BY
Divides the result set into subsets (partitions) for the window function to operate on.


ORDER BY 
Determines the sequence of rows within each partition

 But for ROW_NUMBER() or RANK() — ORDER BY is mandatory