SELECT *
FROM customers;

SELECT *
FROM orders;

-- Inner Join

SELECT *
FROM customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id;