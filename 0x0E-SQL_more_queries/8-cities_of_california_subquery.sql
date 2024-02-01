-- Script lists all the cities of California that can be found in a specified database
-- Lists all the cities of California that can be found in hbtn_0c_usa database
SELECT id, name
FROM cities
WHERE state_id = (
	SELECT id
	FROM states
	WHERE name = 'California'
)
ORDER BY id ASC;
