-- Selecting rows that have id = 89
USE hbtn_0c_0;
SELECT COUNT(id) FROM first_table GROUP BY id HAVING id = 89;
