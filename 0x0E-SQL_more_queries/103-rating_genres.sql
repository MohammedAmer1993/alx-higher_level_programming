-- genres by ratings

SELECT name , sum(rate) as rating from tv_genres
INNER JOIN tv_show_genres on tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows on tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_show_ratings on tv_shows.id = tv_show_ratings.show_id
group by name;
