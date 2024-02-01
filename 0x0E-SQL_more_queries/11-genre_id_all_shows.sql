-- Script lists all shows contained in a database with their genre ids
-- List all shows in hbtn_0d_tvshows database with their genre ids
SELECT title, genre_id
	FROM tv_shows
	LEFT JOIN tv_show_genres
	ON tv_shows.id = tv_show_genres.show_id
	ORDER BY title, genre_id;
