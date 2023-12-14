-- Script updates a record in a specified table in a MySQL databse
-- Update Bob's score to 10 in second_table in hbtn_0c_0 database
UPDATE second_table
	SET score = 10
	WHERE name = 'Bob'
