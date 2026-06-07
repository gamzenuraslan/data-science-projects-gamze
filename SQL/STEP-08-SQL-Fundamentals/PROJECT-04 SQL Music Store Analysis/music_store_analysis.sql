-- Total number of customers
SELECT COUNT(*) AS TotalCustomers
FROM Customer;

------------------------------------

-- Customers by country
SELECT
    Country,
    COUNT(*) AS CustomerCount
FROM Customer
GROUP BY Country
ORDER BY CustomerCount DESC;

------------------------------------

-- Top country by number of customers
SELECT TOP 1
    Country,
    COUNT(*) AS CustomerCount
FROM Customer
GROUP BY Country
ORDER BY CustomerCount DESC;

------------------------------------

-- Countries generating the highest revenue
SELECT
    BillingCountry,
    SUM(Total) AS TotalRevenue
FROM Invoice
GROUP BY BillingCountry
ORDER BY TotalRevenue DESC;

------------------------------------

-- Top customer by spending
SELECT
    c.FirstName,
    c.LastName,
    SUM(i.Total) AS TotalSpent
FROM Customer c
JOIN Invoice i
    ON c.CustomerId = i.CustomerId
GROUP BY
    c.FirstName,
    c.LastName
ORDER BY TotalSpent DESC;

------------------------------------

-- Most popular genres
SELECT
    g.Name AS Genre,
    COUNT(il.InvoiceLineId) AS TotalSales
FROM InvoiceLine il
JOIN Track t
    ON il.TrackId = t.TrackId
JOIN Genre g
    ON t.GenreId = g.GenreId
GROUP BY g.Name
ORDER BY TotalSales DESC;

------------------------------------

-- Top-selling artists
SELECT
    ar.Name AS Artist,
    COUNT(il.InvoiceLineId) AS TotalSales
FROM InvoiceLine il
JOIN Track t
    ON il.TrackId = t.TrackId
JOIN Album al
    ON t.AlbumId = al.AlbumId
JOIN Artist ar
    ON al.ArtistId = ar.ArtistId
GROUP BY ar.Name
ORDER BY TotalSales DESC;

------------------------------------

-- Top-selling tracks
SELECT TOP 10
    t.Name AS Track,
    COUNT(il.InvoiceLineId) AS TotalSales
FROM InvoiceLine il
JOIN Track t
    ON il.TrackId = t.TrackId
GROUP BY t.Name
ORDER BY TotalSales DESC;

------------------------------------

-- Genres generating the highest revenue
SELECT
    g.Name AS Genre,
    SUM(il.UnitPrice * il.Quantity) AS Revenue
FROM InvoiceLine il
JOIN Track t
    ON il.TrackId = t.TrackId
JOIN Genre g
    ON t.GenreId = g.GenreId
GROUP BY g.Name
ORDER BY Revenue DESC;

-------------------------------------

-- Customers supported by each employee
SELECT
    e.FirstName + ' ' + e.LastName AS Employee,
    COUNT(c.CustomerId) AS CustomerCount
FROM Employee e
JOIN Customer c
    ON e.EmployeeId = c.SupportRepId
GROUP BY
    e.FirstName,
    e.LastName
ORDER BY CustomerCount DESC;

