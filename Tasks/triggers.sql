DELIMITER //
CREATE TRIGGER add_app
AFTER INSERT ON application
FOR EACH ROW
BEGIN
    UPDATE actor_apps
    SET num_apps = num_apps + 1
    WHERE id_actor = NEW.id_actor;
END;
//
DELIMITER ;


DELIMITER //
CREATE TRIGGER delete_app
AFTER DELETE ON application
FOR EACH ROW
BEGIN
    UPDATE actor_apps
    SET num_apps = num_apps - 1
    WHERE id_actor = OLD.id_actor;
END;
//
DELIMITER ;


DELIMITER //
CREATE TRIGGER add_actor
AFTER INSERT ON actor
FOR EACH ROW
BEGIN
    INSERT INTO actor_apps (id_actor, surname, name, patronymic, num_apps)
    VALUES (NEW.id_actor, NEW.surname, NEW.name, NEW.patronymic, 0);
END;
//
DELIMITER ;


4. 
DELIMITER //

CREATE TRIGGER delete_actor
AFTER DELETE ON actor
FOR EACH ROW
BEGIN
    DELETE FROM actor_apps
    WHERE id_actor = OLD.id_actor;
END;

//
DELIMITER ;

DELIMITER //
CREATE TRIGGER update_actor
AFTER UPDATE ON actor
FOR EACH ROW
BEGIN
	UPDATE actor_apps
	SET surname = NEW.surname,
		name = NEW.name,
		patronymic = NEW.patronymic
	WHERE id_actor = NEW.id_actor;
END; //
DELIMITER ;

