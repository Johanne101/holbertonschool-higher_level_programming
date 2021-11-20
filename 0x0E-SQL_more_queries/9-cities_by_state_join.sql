-- script lists all cities contained in hbtn_0d_usa
-- Each record should display: cities.id - cities.name - states.name
-- Results must be sorted in ascending order by cities.id
-- You can use only one SELECT statement
SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.state.id = state.id ORDER BY cities.id ASC;
