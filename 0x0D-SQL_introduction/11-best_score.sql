-- Script lists all records with score>=10 in a table in a MySQL database
-- Lists all records with scores>=10 in table second_table in database hbtn_0c_0
SELECT score, name
	FROM second_table
	WHERE score >= 10
	ORDER BY score DESC;

