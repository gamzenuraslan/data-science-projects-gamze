/*
========================================
STEP 08 - SQL Fundamentals
Lesson 02 - WHERE Statement
========================================

Topics covered:
- Filtering rows
- Equal to (=)
- Greater than (>)
- Less than (<)
- Greater than or equal to (>=)
- Filtering text values
*/

-- Employees with salary equal to 5000
SELECT *
FROM Employees
WHERE Salary = 5000;

-- Employees with salary greater than 5000
SELECT *
FROM Employees
WHERE Salary > 5000;

-- Employees with salary less than 5000
SELECT *
FROM Employees
WHERE Salary < 5000;

-- Employees working in the Data department
SELECT *
FROM Employees
WHERE Department = 'Data';

-- Employees with salary greater than or equal to 5000
SELECT Name, Salary
FROM Employees
WHERE Salary >= 5000;