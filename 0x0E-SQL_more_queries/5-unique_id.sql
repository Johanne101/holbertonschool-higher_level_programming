-- Creates a new table with unique Id descriptions
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1, name VARCHAR(256), UNIQUE(id));
