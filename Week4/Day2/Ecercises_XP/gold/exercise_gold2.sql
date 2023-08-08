-- update students set birth_date = '1998-11-02'
-- where last_name = 'Benichou';

-- update students set last_name = 'Guez'
-- where first_name = 'David';

-- delete from students
-- where first_name = 'Lea' and last_name = 'Benichou';

-- select count(id) from students;

-- select count(id) from students where birth_date > '2000-01-01';

-- alter table students add math_grade smallint;

-- update students set math_grade = 80 where id = 1;

-- update students set math_grade = 90 where id in (2,4);

-- update students set math_grade = 40 where id = 6;

-- select count(id) as num_students from students
-- where math_grade > 83;

-- insert into students (first_name, last_name, birth_date, math_grade)
-- values ('Omer', 'Simpson', '1998-11-02', 70);

-- select concat(first_name, ' ', last_name) as student, count(math_grade) as total_grade
-- from students
-- group by student;

select sum(math_grade) as all_grades from students;

