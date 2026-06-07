/*
========================================
STEP 08 - SQL Fundamentals
Lesson 01 - SELECT Statement
========================================

In this lesson, we practice the SQL SELECT statement.

Topics covered:
- Creating a sample table
- Inserting sample data
- Selecting all columns
- Selecting specific columns
- Selecting multiple columns
- Understanding table and column references
*/

IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'proProjeler')
BEGIN
    EXEC('CREATE DATABASE proProjeler');
END
GO

USE proProjeler;
GO

DROP TABLE IF EXISTS Employees;
GO

CREATE TABLE Employees (
    EmployeeID INT,
    Name VARCHAR(50),
    Department VARCHAR(50),
    Salary INT
);

-- Insert sample data into Employees table
INSERT INTO Employees (EmployeeID, Name, Department, Salary)
VALUES
(1, 'Gamze', 'Data', 5000),
(2, 'Ali', 'Sales', 4000),
(3, 'Ayse', 'HR', 4500),
(4, 'Mehmet', 'IT', 6000),
(5, 'Zeynep', 'Marketing', 5500);

-- Select all columns from the Employees table
SELECT *
FROM Employees;

-- Select only employee names
SELECT Name
FROM Employees;

-- Select employee names and departments
SELECT Name, Department
FROM Employees;

-- Select employee names and salaries
SELECT Name, Salary
FROM Employees;

-- Select multiple columns
SELECT EmployeeID, Name, Department, Salary
FROM Employees;