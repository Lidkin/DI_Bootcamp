-- 1. select * from customer

-- select first_name + last_name as full_name from customer; <shood will work. but didn't

-- 2.select first_name || ' ' || last_name as full_name from customer;

-- 2. select concat(first_name, ' ', last_name) as full_name from customer;

-- 3. select distinct(create_date) from customer;

-- 4. select first_name, last_name, email from customer order by first_name;

-- 5. select film_id, title, description, release_year, rental_rate from film order by rental_rate;

-- 6. select address, phone from address where district = 'Texas';

-- 7. select title, description, release_year from film where film_id = 15 or film_id = 150;

-- 7. select title, description, release_year from film where film_id in(15,150);

-- 8. select film_id, title, description, length, rental_rate from film where title in('Enemy Odds', 'Malkovich Pet');

-- 9. select film_id, title, description, length, rental_rate from film where title ilike'ma%';

-- 10. select film_id, title, rental_rate from film order by rental_rate fetch first 10 rows only; 

-- 11. select film_id, title, rental_rate from film order by rental_rate fetch first 10 rows only offset 10; 

-- 12. select concat(customer.first_name, ' ', customer.last_name) as full_name, payment.payment_date, payment.amount 
-- from customer
-- inner join payment on customer.customer_id = payment.customer_id;

-- 13. select film.title, inventory.inventory_id from film
-- left join inventory
-- on film.film_id = inventory.film_id
-- where inventory.inventory_id is null;

-- 14. select city.city, country.country from city
-- inner join country on city.country_id = country.country_id;

select customer.customer_id, concat(customer.first_name, ' ', customer.last_name) as full_name, payment.amount, payment.payment_date, payment.staff_id
from customer
inner join payment
on customer.customer_id = payment.customer_id
order by payment.staff_id;