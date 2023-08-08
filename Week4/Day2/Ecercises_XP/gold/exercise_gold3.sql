-- create table purchases(
-- id serial primary key,
-- 	customer_id smallint references customers(id),
-- 	item_id smallint references items(id),
-- 	quantity_purchased smallint
-- )

-- insert into purchases(customer_id, item_id, quantity_purchased)
-- values 
-- (3, 3, 1),
-- (5, 2, 1),
-- (1, 1, 2);

-- select * from purchases;

-- select * from purchases
-- inner join customers
-- on purchases.customer_id = customers.id;

-- select purchases.quantity_purchased, concat(customers.customer_name, ' ', customers.last_name) as customer
-- from purchases
-- inner join customers
-- on purchases.customer_id = customers.id
-- where customers.id = 5;

-- select purchases.quantity_purchased, items.items
-- from items
-- inner join purchases
-- on purchases.item_id = items.id
-- where items.items in ('Small Desk', 'Large desk');

-- select customers.customer_name, customers.last_name, items.items
-- from customers
-- inner join purchases
-- on customers.id = purchases.customer_id
-- inner join items
-- on items.id = purchases.item_id;

insert into purchases(customer_id, item_id)
values (4, null);
