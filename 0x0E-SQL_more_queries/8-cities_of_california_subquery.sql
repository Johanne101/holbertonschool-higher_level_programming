-- script lists all the cities of California that can be found in the database hbtn_0d_usa
-- /1/ SELECT  /2/FROM INFORMATION_SCHEMA.TABLES /3/WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_CATALOG='YOUR_Database_name'
--
-- The states table contains only one record where name = California (but the id can be different, as per the example)
-- /2/ SELECT states(table) FROM 
-- Results must be sorted in ascending order by cities.id 
-- /3/ ORDER BY cities.id ASC;
SELECT id, name FROM cities WHERE state_id IN ('states') ORDER BY cities.id ASC;
