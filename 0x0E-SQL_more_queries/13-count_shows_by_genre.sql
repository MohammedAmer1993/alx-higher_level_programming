-- select from a table which is a result of a quary

SELECT tv_genres.name as genre, COUNT(tv_show_genres.show_id) as number
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number DESC;






















/*
SELECT b.name AS genre, COUNT(b.show_id) AS number FROM  
(SELECT tv_genres.name, tv_show_genres.genre_id, tv_show_genres.show_id FROM tv_show_genres 
 INNER JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id) AS b 
 GROUP BY genre 
 ORDER BY number DESC;
*/

