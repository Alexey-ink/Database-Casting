CREATE VIEW director_view AS
    SELECT d.id_director, d.name, d.surname, 
           COUNT(DISTINCT f.id_film) AS film_count, 
           COUNT(DISTINCT act.id_actor) AS actor_count
    FROM director AS d
    JOIN film AS f ON d.id_director = f.id_director
    JOIN role AS r ON f.id_film = r.id_film
    JOIN application AS app ON r.id_role = app.id_role
    JOIN actor AS act ON app.id_actor = act.id_actor
    GROUP BY d.id_director, d.name, d.surname;