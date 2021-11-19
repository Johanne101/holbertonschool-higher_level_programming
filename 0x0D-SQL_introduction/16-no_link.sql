-- Script lists all records of table second_table in hbtn_0c_0
-- Don’t list rows without a name value
-- Display "score" and "name" (in this order)
-- Records should be listed by descending score
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
