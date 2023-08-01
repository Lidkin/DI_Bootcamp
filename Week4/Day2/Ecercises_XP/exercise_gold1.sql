-- Exercise 1
-- select count(film_id), rating from film group by rating order by rating;

-- select title, rating from film where rating in ('G', 'PG-13');

-- select title, rating, length, rental_rate from film

-- where rating in ('G', 'PG-13') and length < 120 and rental_rate < 3.00 order by title;

-- update customer set
-- store_id = 1,
-- last_name = 'Black',
-- email = 'betty.black@sakilacustomer.org',
-- create_date = '2006-03-16'
-- where customer_id = 14;

-- update address set
-- address = '350 Starswood Avenue',
-- district = 'Pennsylvania'
-- where address_id = (select address_id from customer where customer_id = 14);