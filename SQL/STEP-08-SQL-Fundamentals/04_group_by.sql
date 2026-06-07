/*
========================================
STEP 08 - SQL Fundamentals
Lesson 04 - GROUP BY Statement
========================================

Topics covered:
- Grouping rows
- COUNT()
- AVG()
- Aggregating data by category
- Summarizing grouped data
*/

-- List departments
SELECT Department
FROM Employees
GROUP BY Department;

-- Count employees in each department
SELECT Department, COUNT(*) AS EmployeeCount
FROM Employees
GROUP BY Department;

-- Average salary by department
SELECT Department, AVG(Salary) AS AverageSalary
FROM Employees
GROUP BY Department;

-- Highest salary by department
SELECT Department, MAX(Salary) AS HighestSalary
FROM Employees
GROUP BY Department;