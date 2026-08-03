Select 
    c.name AS Customers
FROM Customers AS c
LEFT JOIN 
Orders AS o
    ON 
    c.id = o.customerID
WHERE customerID IS NULL;