-- a script that converts hbtn_0c_0 database to UTF8
-- (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.

ALTER DATABASE IF EXISTS first_table CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE IF EXISTS first_table CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE first_table MODIFY
    name VARCHAR(256)
    COLLATE utf8_general_ci;
