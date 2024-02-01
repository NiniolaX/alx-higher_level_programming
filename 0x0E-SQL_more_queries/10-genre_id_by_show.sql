-- Script lists all shows contained in a database that has at least one genre linked
-- List all shows in hbtn_0d_tvshows databse that has a genre linked
SELECT title, genre_id
	FROM tv_show_genres
	INNER JOIN tv_shows
	ON tv_show_genres.show_id = tv_shows.id
	ORDER BY title, genre_id ASC;
