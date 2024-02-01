-- Lists all cities contained in a specified database with each record displaying cities.id - cities.name - states.name
-- Lists all cities contained in the database
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states
ON cities.state_id = states.id;
