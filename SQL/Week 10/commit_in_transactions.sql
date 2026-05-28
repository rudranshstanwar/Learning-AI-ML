SELECT *
FROM accounts;

-- Transactions

START TRANSACTION;

UPDATE accounts 
SET balance = balance - 50 WHERE id = 1;

UPDATE accounts 
SET balance = balance + 50 WHERE id = 2;

COMMIT;