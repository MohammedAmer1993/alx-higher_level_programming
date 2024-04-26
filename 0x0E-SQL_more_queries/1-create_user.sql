-- ADDING USERS AND PRIVILEGES
-- create a new user
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- GRANT PIVILIGES
GRANT ALL ON *.* TO 'user_0d_1'@'localhost';
-- FLUSH
FLUSH PRIVILEGES;
