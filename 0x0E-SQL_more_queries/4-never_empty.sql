-- ID can never be NULL when table is created
CREATE TABLE IF NOT EXISTS id_not_null(id INT DEFAULT 1, name VARCHAR(256));
