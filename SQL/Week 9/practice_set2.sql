USE college;
SET SQL_SAFE_UPDATES = 0;

CREATE TABLE student (
	rollno INT PRIMARY KEY,
    city VARCHAR(30),
    marks INT
);

INSERT INTO student
(rollno, city, marks)
VALUES
(110, "adam", 76),
(108, "bob", 65),
(124, "casey", 94),
(112, "duke", 80);

SELECT *
FROM student
WHERE marks > 75;

SELECT avg(marks)
FROM student;

ALTER TABLE student
ADD COLUMN grade VARCHAR(2);

UPDATE student
SET grade = "O"
WHERE marks >= 80;

UPDATE student
SET grade = "A"
WHERE marks BETWEEN 70 AND 80;

UPDATE student
SET grade = "B"
WHERE marks BETWEEN 60 AND 70;