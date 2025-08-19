
--DROP TABLE IF EXISTS parent;
--CREATE TABLE IF NOT EXISTS parent(
  --  id BIGSERIAL PRIMARY KEY,
    --name VARCHAR(100) NOT NULL,
    --email VARCHAR(250) NOT NULL UNIQUE,
--);

--DROP TABLE IF EXISTS parent_address;
CREATE TABLE IF NOT EXISTS parent_address(
    id BIGSERIAL PRIMARY KEY,
    parent_email VARCHAR REFERENCES parent(email),
    county_name VARCHAR(250),
    town VARCHAR(250),
    longitude REAL,
    latitude REAL,
    house_no VARCHAR(200)
);

--INSERT INTO parent
  --  (name, email)
--VALUES
  -- ('John Doe', 'johndoe@gmail.com')

--INSERT INTO parent_address  
  --  (parent_id, county_name, town, longitude, latitude, house_no)
--VALUES
  --  (1, 'County A', 'Town X', 12.3456, 65.4321, '123A')