-- create database
CREATE DATABASE IF NOT EXISTS hbtn_0c_0;
-- use database
USE hbtn_0c_0;
-- create table
CREATE TABLE IF NOT EXISTS first_table (
    name VARCHAR(256)
);
-- change every thing into utf8
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- edit table 
ALTER TABLE first_table CONVERT TO CHARACTER SET
utf8mb4 COLLATE utf8mb4_unicode_ci;
-- alter column
ALTER TABLE first_table MODIFY name VARCHAR(256)
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
