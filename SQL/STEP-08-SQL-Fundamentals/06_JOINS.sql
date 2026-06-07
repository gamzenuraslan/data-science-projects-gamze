/*
========================================
STEP 08 - SQL Fundamentals
Lesson 06 - JOIN Statement
========================================

Topics covered:
- INNER JOIN
- Combining data from multiple tables
- Matching related records
- Using aliases
- Real-world relational database concepts
*/

-- Create Departments table
CREATE TABLE Departments (
    DepartmentID INT,
    DepartmentName VARCHAR(50)
);

-- Insert sample data
INSERT INTO Departments
VALUES
(1, 'Data'),
(2, 'Sales'),
(3, 'HR');

-- Join Employees and Departments
SELECT
    e.Name,
    d.DepartmentName
FROM Employees e
INNER JOIN Departments d
    ON e.DepartmentID = d.DepartmentID;