-- Script lists the number of records with the same score in a specified table of a database
-- Lists number of records with same score in the table second_table
SELECT score, COUNT(score) as number
	FROM second_table
	GROUP BY score
	ORDER BY number DESC;
