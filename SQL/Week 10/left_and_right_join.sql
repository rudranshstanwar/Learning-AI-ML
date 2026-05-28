SELECT *
FROM customers;

SELECT *
FROM orders;

-- Left Join

SELECT *
FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id;

-- Right Join

SELECT *
FROM customers c
RIGHT JOIN orders o
ON c.customer_id = o.customer_id;