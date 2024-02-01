-- Script lists all the genres of tv show 'Dexter' in a given database
-- Lists all the genres of tv show 'Dexter' in the hbtn_0d_tvshows database
SELECT name FROM tv_genres
	INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
	INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
	WHERE tv_shows.title = 'Dexter'
	ORDER BY name ASC;
