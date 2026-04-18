SELECT * FROM TABLE(RESULT_SCAN('your_query_id'));  -- result of a query

SELECT LAST_QUERY_ID();

SELECT * FROM table_name BEFORE (STATEMENT => 'truncate_query_id');