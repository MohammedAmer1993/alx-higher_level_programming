-- create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- select database
USE hbtn_0d_usa;

-- create table
CREATE TABLE IF NOT EXISTS states (
    id INT UNIQUE NOT NULL PRIMARY KEY AOUT_INCREMENT,
    name VARCHAR(256) NOT NULL
);
