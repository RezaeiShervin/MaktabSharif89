------------------------ 5 ------------------------
-- select *
-- from customer
-- join address
-- on customer.address_id = address.address_id
-- join city
-- on address.city_id = city.city_id
-- join country
-- on city.country_id = country.country_id
-- where country = 'Brazil'
-- order by city;


------------------------ 7 ------------------------
-- select *
-- from film
-- join inventory
-- on film.film_id = inventory.film_id
-- left join rental
-- on inventory.inventory_id = rental.inventory_id


------------------------ 8 ------------------------
-- select *
-- from customer
-- left join rental
-- on customer.customer_id = rental.customer_id


------------------------ 9 ------------------------
-- select title, count(*) as number
-- from film
-- join inventory
-- on film.film_id = inventory.film_id
-- join rental
-- on inventory.inventory_id = rental.inventory_id
-- group by title


------------------------ 10 -----------------------
-- select concat(first_name, last_name) as actor_name, count(*)
-- from actor
-- join film_actor
-- on actor.actor_id = film_actor.actor_id
-- group by concat(first_name, last_name)
-- having count(*) > 20 


---------------------- 1 ------------------------
-- select title, concat(first_name, last_name) as actor_name, length
-- from actor
-- join film_actor
-- on actor.actor_id = film_actor.actor_id
-- join film 
-- on film.film_id = film_actor.film_id
-- where length > 60


------------------------ 2 ------------------------
-- select actor.actor_id, concat(first_name, last_name), count(*)
-- from actor
-- join film_actor
-- on actor.actor_id = film_actor.actor_id
-- group by actor.actor_id 
-- order by actor.actor_id 










