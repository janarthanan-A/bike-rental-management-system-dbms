-- Create database if not exists
CREATE DATABASE db3;

-- Use the db3 database
USE db3;

-- Create bikes table
CREATE TABLE bikes (
    bike_id INT PRIMARY KEY,
    model VARCHAR(255) NOT NULL,
    brand VARCHAR(100) NOT NULL,
    price_per_hour DECIMAL(10, 2) NOT NULL
);

-- Sample bike data
INSERT INTO bikes (bike_id, model, brand, price_per_hour) VALUES
(101, 'GT-650', 'ROYAL ENFIELD', 15.00),
(102, 'SHINE', 'HONDA', 10.00),
(103, 'ACTIVA 6G', 'HONDA', 10.00),
(104, 'OLA  AD1', 'OLA', 13.00),
(105, 'MT-15', 'YAMAHA', 13.00);
 select * from bikes;
