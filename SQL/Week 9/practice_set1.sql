USE college;
SET SQL_SAFE_UPDATES = 0;

CREATE TABLE teacher (
	id INT,
    name VARCHAR(20),
    sub VARCHAR(10),
    salary INT,
    PRIMARY KEY(id)
);

INSERT INTO teacher
(id, name, sub, salary)
VALUES
(23, "ajay", "math", 50000),
(47, "bharat", "english", 60000),
(18, "chetan", "chemistry", 45000),
(9, "divya", "physics", 75000);

SELECT *
FROM teacher;

ALTER TABLE teacher
CHANGE COLUMN salary ctc INT DEFAULT 0;

UPDATE teacher
SET ctc = ctc + 0.25 * ctc;

ALTER TABLE teacher
ADD COLUMN city VARCHAR(50) DEFAULT "gurgaon";

ALTER TABLE teacher
DROP COLUMN ctc;