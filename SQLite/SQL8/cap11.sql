-- Queries

-- Matching customers and salesmen by city
SELECT Customer.cust_name, Salesmen.name, Salesmen.city
FROM Customer
JOIN Salesmen ON Salesmen.salesmen_id = Customer.salesmen_id;

--Linking customers to their salesmen
SELECT Customer.cust_name, Salesman.name
FROM Customer
JOIN Salesman ON Customer.Salesman_id =Salesman.Salesman_id;

-- Fetching orders where customer's city does not match salesman's city
SELECT Orders.ord_no, Customer.cust_name, Orders.customer_id, Orders.Salesman_id
FROM Orders
JOIN Customer ON Orders.customer_id = Customer.customer_id
JOIN Salesman ON Orders.Salesman_id = Salesman.Salesman_id
WHERE Customer.city <> Salesman.city;

-- Fetching all orders with customer names
SELECT Orders.ord_no, Customer.cust_name
FROM Orders
JOIN Customer ON Orders.customer_id = Customer.customer_id;

-- Customers with grades
SELECT Customer.cust_name AS "Customer", Customer.grade AS "Grade"
FROM Orders
JOIN Salesman ON Orders.Salesman_id = Salesman.Salesman_id
JOIN Customer ON Orders.customer_id = Customer.customer_id
WHERE Customer.grade IS NOT NULL;

-- Customers with salesmen where commission is between 0.12 and 0.14
SELECT Customer.cust_name AS "Customer",
Customer.city AS "City",
Salesman.name AS "Salesman",
Salesman.Comission
FROM Customer
JOIN Salesman ON Customer.Salesman_id = Salesman.Salesman_id
WHERE Salesman.Comission BETWEEN 0.12 AND 0.14;

-- Calculating commissions for orders where customer grade is 200 or more
SELECT Orders.ord_no, Customer.cust_name, Salesman.Comission AS "Commission%",
Orders.purch_amt * Salesman.Comission AS "Commission"
FROM Orders
JOIN Salesman ON Orders.Salesman_id = Salesman.Salesman_id
JOIN Customer ON Orders.customer_id = Customer.customer_id
WHERE Customer.grade >= 200;

-- Orders on a specific date
SELECT *
FROM Customer
JOIN Orders ON Customer.customer_id = Orders.customer_id
WHERE Orders.ord_date = '2012-10-05';
