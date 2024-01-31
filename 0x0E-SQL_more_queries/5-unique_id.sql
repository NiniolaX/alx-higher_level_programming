-- Creates a table with a unique attribute
-- Create a table unique_id with a unique attribute
CREATE TABLE IF NOT EXISTS unique_id(
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
	);
