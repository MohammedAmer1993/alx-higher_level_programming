-- list all with some conditions
SELECT score, name FROM second_table
ORDER BY score DESC
WHERE name IS NOT NULL;
