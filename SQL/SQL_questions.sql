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

