-- creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server
-- creates a database
CREATE database IF NOT EXISTS hbtn_0d_usa;
-- use a database
USE hbtn_0d_usa;
-- create table
CREATE TABLE IF NOT EXISTS cities (
id INT UNIQUE AUTO_INCREMENT NOT NULL,
state_id INT NOT NULL,
name VARCHAR(256) NOT NULL, PRIMARY KEY(id),  FOREIGN KEY(state_id) REFERENCES states(id))