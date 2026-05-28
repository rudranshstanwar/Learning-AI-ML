SELECT *
FROM customers;

SELECT *
FROM orders;

-- Self Join

SELECT *
FROM customers a
JOIN customers b
ON a.customer_id = b.customer_id;