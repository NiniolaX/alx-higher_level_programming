-- Script removes all records with a certain condition from a specified table in a MySQL database
-- Removes records with score <= 5 from second_table
DELETE FROM second_table
	WHERE score <= 5;
