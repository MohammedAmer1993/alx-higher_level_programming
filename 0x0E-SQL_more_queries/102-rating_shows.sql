-- show the ratings of every show
SELECT title , sum(rate) AS rating FROM tv_shows
INNER JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.show_id
GROUP BY title
ORDER BY rating DESC;
