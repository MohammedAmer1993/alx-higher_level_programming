-- select the best
USE hbtn_0c_0;
SELECT score, name FROM second_table
ORDER BY score ASC
WHERE score >= 10;
