-- script lists all records of second_table in hbtn_0c_0 DB
-- Results should display both the score and the name (in this order)
-- Records should be ordered by score (top first)
-- The database name will be passed as an argument of the mysql command
SELECT score, name FROM second_table ORDER BY score DESC;
