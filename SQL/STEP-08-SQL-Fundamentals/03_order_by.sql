/*
========================================
STEP 08 - SQL Fundamentals
Lesson 03 - ORDER BY Statement
========================================

Topics covered:
- Sorting data
- Ascending order (ASC)
- Descending order (DESC)
- Sorting text values
- Combining WHERE and ORDER BY
*/

-- Sort employees by salary (ascending)
SELECT *
FROM Employees
ORDER BY Salary ASC;

-- Sort employees by salary (descending)
SELECT *
FROM Employees
ORDER BY Salary DESC;

-- Sort employees by name
SELECT *
FROM Employees
ORDER BY Name ASC;

-- Employees with salary greater than or equal to 4500
-- sorted by salary (highest to lowest)
SELECT Name, Salary
FROM Employees
WHERE Salary >= 4500
ORDER BY Salary DESC;