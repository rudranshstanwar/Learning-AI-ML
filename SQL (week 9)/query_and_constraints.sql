CREATE DATABASE IF NOT EXISTS instagram;

USE instagram;

CREATE TABLE user (
	id INT ,
    age INT,
    name VARCHAR(30) NOT NULL,
    email VARCHAR(50) UNIQUE,
    followers INT DEFAULT 0,
    following INT DEFAULT 0,
    CONSTRAINT age_check CHECK (age >= 13),
    PRIMARY KEY (id)
);

INSERT INTO user
(id, age, name, email, followers, following)
VALUES
(1, 14, "adam", "adam@yahoo.in", 123, 145),
(2, 15, "bob", "bob123@gmail.com", 200, 200),
(3, 16, "casey", "casey@email.com", 300, 306),
(4, 17, "donald", "donald@gmailcom", 200, 105);

INSERT INTO user
(id, age, name, email, followers, following)
VALUES
(5, 14, "eve", "eve@yahoo.in", 400, 145),
(6, 16, "farah", "farah@gmail.com", 10000, 1000);

SELECT name, age, followers 
FROM user
WHERE age > 15 OR followers > 200;


CREATE TABLE post (
	id INT PRIMARY KEY,
    content VARCHAR(100),
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES user(id)
);

INSERT INTO post 
VALUES
(101, "Hello World", 3),
(102, "Bye Bye", 1),
(103, "Hello Delta", 3);