
--DROP TABLE IF EXISTS hostel;
--CREATE TABLE hostel(
    --id BIGSERIAL PRIMARY KEY,
    --student_id INTEGER REFERENCES student(id) NOT NULL UNIQUE,
    --name TEXT,
  --  room TEXT    
--)

--CREATE TABLE sports(
    --id BIGSERIAL PRIMARY KEY,
   -- student_id INTEGER REFERENCES student(id) NOT NULL UNIQUE,
    --name TEXT,
  --  room TEXT    
--)

--CREATE TABLE subject(
    --id BIGSERIAL PRIMARY KEY,
  --  name TEXT   
--)

--CREATE TABLE student_subject(
  --  id BIGSERIAL PRIMARY KEY,
    --student_id INTEGER NOT NULL REFERENCES student(id),
    --subject_id BIGINT NOT NULL REFERENCES subject(id),
    --UNIQUE(student_id,subject_id)
--)

INSERT INTO subject (name)
VALUES 
('English'),
('Math'),
('Physics'),
('History')

--ON DELETE CASCADE<student>
--sport ON DELETE SET NULL;
--ON DELETE RESTRICTION;