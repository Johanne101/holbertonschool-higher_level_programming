-- Script lists number of records w/the same score in second_table of hbtn_0c_0
-- The result should display:
-- the score count(*) from second_table
-- the number of records of `score` labeled "number"
-- The list should be sorted by the number of records (descending)
SELECT score, COUNT(score) 'number' FROM second_table GROUP BY score ORDER BY 'number' DESC;
