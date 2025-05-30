-- Benign query
SELECT name, age FROM users WHERE id = 42;

-- Potentially risky query
SELECT * FROM customers;

-- Dynamic SQL (high risk)
EXECUTE('SELECT * FROM ' || tablename);

-- No WHERE clause on DELETE
DELETE FROM transactions;

-- Parameterized query (good practice)
SELECT * FROM orders WHERE order_id = ?;
