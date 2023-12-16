-- Script lists all records of a specified table in a specified order without listing records with NULL values for a specified attribute
-- List all records of table second_table,
--	without displaying records without a name value,
--	displaying score and name columns (in this order),
-- 	listing records by descending score.
SELECT score, name
	FROM second_table
	WHERE name IS NOT NULL
	ORDER BY score DESC;
