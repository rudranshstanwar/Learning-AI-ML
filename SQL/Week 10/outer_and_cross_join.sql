SELECT *
FROM customers;

SELECT *
FROM orders;

-- Outer Join

SELECT *
FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id
UNION
SELECT *
FROM customers c
RIGHT JOIN orders o
ON c.customer_id = o.customer_id;

-- Cross Join

SELECT *
FROM customers c
CROSS JOIN orders o;