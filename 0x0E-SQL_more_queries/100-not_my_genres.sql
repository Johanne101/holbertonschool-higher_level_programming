-- script uses tvshows DB to;
-- list all genres not linked to the show Dexter
-- The tv_shows table contains only one record where title = Dexter (id can differ)
-- Should display(SELECT): tv_genres.name
-- Results sorted: order by the genre name ASC;
SELECT tv_genres.name FROM tv_genres
WHERE tv_genres.name NOT IN (
	SELECT tv_genres.name FROM tv_genres
	INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
	INNER JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
	WHERE tv_shows.title = "Dexter")
ORDER BY tv_genres.name ASC;
