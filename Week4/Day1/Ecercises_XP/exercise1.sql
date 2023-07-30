-- create table items (
--     id serial primary key,
-- 	furniture varchar,
-- 	price int
-- )

-- create table customers (
--     id serial primary key,
-- 	customer_name varchar,
-- 	last_name varchar
-- )

-- ALTER TABLE items ALTER COLUMN price TYPE float;

-- insert into items(furniture, price)
-- values
--    ('Small Desk', 100),
--    ('Large desk', 300),
--    ('Fan ', 80)
   
-- insert into customers(customer_name, last_name)
-- values
--    ('Greg ', 'Jones'),
--    ('Sandra', 'Jones'),
--    ('Scott', 'Scott'),
--    ('Trevor', 'Green'),
--    ('Melanie', 'Johnson')
   
-- ALTER TABLE items RENAME COLUMN furniture TO items;  

-- select * from items

-- select * from items where price > 80

-- select * from items where price <= 300

-- select * from customers where last_name = 'Smith'

-- select * from customers where last_name = 'Jones' 

select * from customers where customer_name != 'Scott'
   