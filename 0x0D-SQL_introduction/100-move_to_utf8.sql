-- Script converts hbtn_0c_0 to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
-- convert all of the following to `UTF8`:
-- 1. Database `hbtn_0c_0`
-- 2. Table `first_table`
-- 3. Field `name` in `first_table`
-- ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8 COLLATE utf8mb4_unicode_ci;
ALTER TABLE hbtn_0c_0.first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;


-- ALTER TABLE hbtn_0c_0.first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- SELECT name, CONVERT(name USING utf8) as anyVariableName FROM first_table;

