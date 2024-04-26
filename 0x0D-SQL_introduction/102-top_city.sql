-- top 3 in aug and jul
SELECT city, ROUND(AVG(vv), 4) AS avg_temp FROM 
(SELECT city , MONTH, ROUND(AVG(value), 5) AS vv FROM temperatures GROUP BY city, month HAVING month = 7 OR month = 8) AS subqu 
GROUP BY city 
ORDER BY avg_temp DESC 
LIMIT 3 ;
