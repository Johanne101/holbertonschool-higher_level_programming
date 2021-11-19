-- script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.
-- cities description:
-- id INT unique, auto generated, can’t be null and is a primary key
-- state_id INT, can’t be null and must be a FOREIGN KEY that references to id of the states table
-- name VARCHAR(256) can’t be null
-- If the database hbtn_0d_usa already exists, your script should not fail
-- If the table cities already exists, your script should not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities
(
	id INT NOT NULL AUTO_INCREMENT,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	UNIQUE(id),
	PRIMARY KEY(id),
	FOREIGN KEY(state_id) REFERENCES states(id));

-- CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
-- `id` INT NOT NULL AUTO_INCREMENTED PIMARY KEY,
--	`state_id` INT NOT NULL ,
--	`name` VARCHAR(256) NOT NULL,
-- FOREIGN KEY (fk_field1, fk_field2) REFERENCES table2 (t2_fieldA, t2_fieldB))
