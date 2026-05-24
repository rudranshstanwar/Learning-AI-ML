USE instagram;
SET SQL_SAFE_UPDATES = 0;

SELECT name, age, email
FROM user
WHERE age > 14
LIMIT 2;

SELECT name, age, followers
FROM user
ORDER BY followers ASC;

SELECT max(followers)
FROM user;

SELECT count(age)
FROM user
WHERE age = 14;

SELECT age, max(followers)
FROM user
GROUP BY age
HAVING max(followers) > 200;

UPDATE user
SET followers = 600
WHERE age = 16;

ALTER TABLE user
ADD COLUMN CITY VARCHAR(25) DEFAULT "Delhi";

ALTER TABLE user
RENAME TO instaUser;

ALTER TABLE instaUser
RENAME TO user;