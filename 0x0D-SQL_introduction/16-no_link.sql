-- list all with some conditions
USE hbtn_0c_0;
SELECT score, name FROM second_table
ORDER BY score DESC
WHERE name IS NOT NULL;
