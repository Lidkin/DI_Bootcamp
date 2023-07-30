-- create table students(
--     id serial primary key,
-- 	last_name varchar,
-- 	first_name varchar,
-- 	birth_date date
-- );

-- insert into students(last_name, first_name, birth_date)
-- values
--    ('Marc',	'Benichou',	'1998-02-11'),
--    ('Yoan',	'Cohen', '2010-12-03'),
--    ('Lea',	'Benichou', '1987-07-27'),
--    ('Amelia', 'Dux', '1996-04-07'),
--    ('David',	'Grez', '2003-06-14'),
--    ('Omer', 'Simpson', '1980-10-03');
   
--    select * from students;

-- select first_name, last_name from students;

-- select first_name, last_name from students where id = 2;

-- ALTER TABLE students RENAME COLUMN first_name TO student_name;
-- ALTER TABLE students RENAME COLUMN last_name TO first_name;
-- ALTER TABLE students RENAME COLUMN student_name to last_name;

-- select first_name, last_name from students where first_name = 'Marc' and last_name = 'Benichou';

-- select first_name, last_name from students where first_name = 'Marc' or last_name = 'Benichou';

-- select first_name, last_name from students where first_name like '%a%';

-- select first_name, last_name from students where first_name ilike 'a%';

-- select first_name, last_name from students where first_name like '%a';

-- select first_name, last_name from students where first_name like '%a_';

-- select first_name, last_name from students where id in(1,3);

select first_name, last_name from students where birth_date >= '2000-01-01'

   
   