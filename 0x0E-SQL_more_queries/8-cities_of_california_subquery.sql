-- lists all the cities of California that can be found in the database hbtn_0d_usa
-- lists all rows of a column in a database
SELECT id , name
FROM cities, states
WHERE  states.name = 'California' AND cities.state_id = states.id 
ORDER BY cities.id ASC