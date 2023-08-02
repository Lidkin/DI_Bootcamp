--part 1:

-- create table customer(
-- id serial primary key,
-- first_name varchar(50) not null,
-- last_name varchar(50) not null
-- );

-- create table profile (
-- id serial primary key,
-- isLoggedIn boolean default false,
-- customer_id int references customer (id)
-- );

-- insert into customer (first_name, last_name)
-- values
-- ('John', 'Doe'),
-- ('Jerome', 'Lalu'),
-- ('Lea', 'Rive')

-- insert into profile (isLoggedIn, customer_id)
-- values
-- (true, 1),
-- (false, 2)

-- select first_name
-- from customer c
-- right join profile p
-- on c.id = p.customer_id;

-- select first_name
-- from customer c
-- full outer join profile p
-- on c.id = p.customer_id;

-- select count(first_name)
-- from customer c
-- left join profile p
-- on c.id = p.customer_id
-- where p.customer_id is null;


-- part 2:

-- create table book (
-- book_id serial primary key,
-- title varchar(100) not null,
-- autor varchar(100) not null
-- );

-- create table student (
-- student_id serial primary key,
-- 	name varchar(100) not null unique,
-- 	age int check (age <= 15)
-- );

-- insert into book(title, autor)
-- values
-- ('Alice In Wonderland', 'Lewis Carroll'),
-- ('Harry Potter', 'J.K Rowling'),
-- ('To kill a mockingbird', 'Harper Lee');

-- insert into student(name, age)
-- values
-- ('John', 12),
-- ('Lera', 11),
-- ('Patrick', 10),
-- ('Bob', 14);

-- create table library (
-- 	book_fk_id int references book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,
-- 	student_id int references student(student_id) ON DELETE CASCADE ON UPDATE CASCADE,
-- 	borrowed_date date not null
-- );
 
-- insert into library(book_fk_id, student_id, borrowed_date)
-- values
-- ((select book.book_id from book where book.title ilike 'a%'), 
-- (select student.student_id from student where student.name ilike 'j%'), '2022-02-15'),
-- ((select book.book_id from book where book.title ilike 't%'), 
-- (select student.student_id from student where student.name ilike 'b%'), '2021-03-03'),
-- ((select book.book_id from book where book.title ilike 'a%'), 
-- (select student.student_id from student where student.name ilike 'l%'), '2021-05-23'),
-- ((select book.book_id from book where book.title ilike 'b%'), 
-- (select student.student_id from student where student.name ilike 'h%'), '2021-08-12')

-- update library
-- set student_id = (select student.student_id from student where student.name ilike 'b%'),
-- book_fk_id = (select book.book_id from book where book.title ilike 'h%')
-- where student_id is null and book_fk_id is null;

-- select * from library;

-- select name, b.title from student s
-- inner join library l
-- on l.student_id = s.student_id
-- inner join book b
-- on l.book_fk_id = b.book_id
-- order by name;

-- select round(avg(age), 2) from student s
-- inner join library l on l.student_id = s.student_id
-- inner join book b on l.book_fk_id = b.book_id
-- where b.title ilike 'a%';

-- delete from student s
-- where s.name ilike 'b%';

select * from library;

