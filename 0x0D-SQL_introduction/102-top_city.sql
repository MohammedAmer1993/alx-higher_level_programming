-- top 3 in aug and jul
CREATE TABLE IF NOT EXISTS temp
    SELECT *
    FROM temperatures
    WHERE month = 7 OR month = 8;
SELECT city, AVG(value) AS avg_temp
FROM temp
GROUP BY city 
ORDER BY avg_temp DESC 
LIMIT 3 ;
