DROP TABLE IF EXISTS student;

CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    dob TEXT,
    phone TEXT,
    marks REAL
);

INSERT INTO student (name, email, dob, phone, marks)
VALUES ('alice', 'alice@gmail.com', '2000-01-01', '9876543210', 85.5);

SELECT * FROM student;
