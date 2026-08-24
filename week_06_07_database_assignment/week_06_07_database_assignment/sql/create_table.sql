-- Bookstore database - Books table
-- Run this in phpMyAdmin (or the MariaDB command line) against your
-- "bookstore" database before running main_program.py

CREATE TABLE IF NOT EXISTS Books (
    Book_ID INT AUTO_INCREMENT PRIMARY KEY,
    Title VARCHAR(255) NOT NULL,
    Author VARCHAR(255) NOT NULL,
    Quantity INT NOT NULL,
    Signed_Edition CHAR(1) NULL,
    Promo_Price FLOAT NULL,
    Retail_Price FLOAT NOT NULL
);
