/*
========================================
STEP 08 - SQL Fundamentals
Lesson 05 - Aggregate Functions
========================================

Topics covered:
- COUNT()
- SUM()
- AVG()
- MIN()
- MAX()
- Basic data summarization
*/

-- Count total employees
SELECT COUNT(*) AS TotalEmployees
FROM Employees;

-- Calculate total salary
SELECT SUM(Salary) AS TotalSalary
FROM Employees;

-- Calculate average salary
SELECT AVG(Salary) AS AverageSalary
FROM Employees;

-- Find the lowest salary
SELECT MIN(Salary) AS LowestSalary
FROM Employees;

-- Find the highest salary
SELECT MAX(Salary) AS HighestSalary
FROM Employees;

-- Summary report
SELECT
    COUNT(*) AS TotalEmployees,
    AVG(Salary) AS AverageSalary,
    MIN(Salary) AS LowestSalary,
    MAX(Salary) AS HighestSalary
FROM Employees;