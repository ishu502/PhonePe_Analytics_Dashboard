CREATE DATABASE phonepeDB;
USE phonepeDB;

CREATE TABLE users (
    UserID VARCHAR(10) PRIMARY KEY,
    State VARCHAR(50),
    Age INT,
    Gender VARCHAR(10)
);

CREATE TABLE transactions (
    TransactionID VARCHAR(15) PRIMARY KEY,
    UserID VARCHAR(10),
    Amount DECIMAL(10,2),
    PaymentType VARCHAR(20),
    TransactionDate DATE,
    FOREIGN KEY (UserID) REFERENCES users(UserID)
);

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/users.csv'
INTO TABLE users
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/transactions.csv'
INTO TABLE transactions
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

SHOW VARIABLES LIKE 'secure_file_priv';
SELECT LOAD_FILE('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/users.csv');

-- Check users table
SELECT COUNT(*) AS total_users FROM users;

SELECT COUNT(*) AS total_transactions FROM transactions;

SELECT SUM(Amount) AS TotalRevenue FROM transactions;

SELECT COUNT(*) AS TotalUsers FROM users;

SELECT PaymentType, COUNT(*) AS TotalTransactions
FROM transactions
GROUP BY PaymentType;

SELECT YEAR(TransactionDate) AS Year, SUM(Amount) AS YearlyRevenue
FROM transactions
GROUP BY YEAR(TransactionDate)
ORDER BY Year;

SELECT State, COUNT(UserID) AS UsersByState
FROM users
GROUP BY State
ORDER BY UsersByState DESC;

SELECT AVG(Amount) AS AvgTransactionValue FROM transactions;

SELECT u.Gender, SUM(t.Amount) AS RevenueByGender
FROM users u
JOIN transactions t ON u.UserID = t.UserID
GROUP BY u.Gender;


