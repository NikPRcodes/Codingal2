SELECT ord_no
FROM Orders
WHERE Salesman_id = (SELECT Salesman_id FROM Salesman WHERE city = 'London');