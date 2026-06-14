SELECT * FROM TABLE(RESULT_SCAN('your_query_id'));  -- result of a query

SELECT LAST_QUERY_ID();

SELECT * FROM table_name BEFORE (STATEMENT => 'truncate_query_id');

SELECT *
FROM table_name
AT (TIMESTAMP => '2026-04-18 10:00:00');