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
    EmployeeID INT PRIMARY KEY,
    Name VARCHAR(50),
    DepartmentName VARCHAR(50),
    DepartmentID INT,
    Salary INT
);

INSERT INTO Employees
VALUES
(1, 'Gamze', 'Data', 1, 5000),
(2, 'Ali', 'Sales', 2, 4000),
(3, 'Ayse', 'HR', 3, 4500),
(4, 'Mehmet', 'Data', 1, 6500),
(5, 'Zeynep', 'Sales', 2, 5500);

-- Create Departments table

CREATE TABLE Department (
    DepartmentID INT,
    DepartmentName VARCHAR(50)
);

-- Insert sample data

INSERT INTO Department
VALUES
(1, 'Data'),
(2, 'Sales'),
(3, 'HR');

SELECT
    DepartmentName,
    COUNT(*) AS EmployeeCount
FROM Employees
GROUP BY DepartmentName;

SELECT
    DepartmentName,
    COUNT(*) AS EmployeeCount
FROM Employees
GROUP BY DepartmentName
HAVING COUNT(*) > 1;

SELECT
    DepartmentName,
    AVG(Salary) AS AverageSalary
FROM Employees
GROUP BY DepartmentName;

SELECT
    DepartmentName,
    AVG(Salary) AS AverageSalary
FROM Employees
GROUP BY DepartmentName
HAVING AVG(Salary) > 5000;

SELECT
    DepartmentName,
    SUM(Salary) AS TotalSalary
FROM Employees
GROUP BY DepartmentName;

SELECT
    DepartmentName,
    SUM(Salary) AS TotalSalary
FROM Employees
GROUP BY DepartmentName
HAVING SUM(Salary) > 9000;

SELECT
    DepartmentName,
    AVG(Salary) AS AverageSalary
FROM Employees
WHERE Salary >= 4500
GROUP BY DepartmentName
HAVING AVG(Salary) > 5000;
