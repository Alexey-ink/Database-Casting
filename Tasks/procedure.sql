DELIMITER // 

CREATE PROCEDURE new_application(
	IN ac_surname varchar(30),
	IN ac_name varchar(20), 
	IN ac_patronymic varchar(20),	
	IN ac_date_of_birth date, 
	IN ac_passport_number varchar(15),
	IN ac_education varchar(100),
	IN ac_work_experience varchar(100),
	IN d_surname varchar(30),
	IN d_name varchar(20), 
	IN d_date_of_birth date, 
	IN d_passport_number varchar(15),
	IN d_awards varchar(100),
	IN id_cas_dir int unsigned,
	IN id_input_role int unsigned
)
BEGIN
	DECLARE act_id INT DEFAULT NULL;
	DECLARE dir_id INT DEFAULT NULL;

	SELECT id_actor INTO act_id
	FROM actor
	WHERE surname = ac_surname AND name = ac_name AND patronymic = ac_patronymic
		AND date_of_birth = ac_date_of_birth;	

	IF act_id IS NULL THEN
		INSERT INTO actor(surname, name, patronymic, date_of_birth, 
				  passport_number, education, work_experience)
			VALUES(ac_surname, ac_name, ac_patronymic, ac_date_of_birth,
				ac_passport_number, ac_education, ac_work_experience);
		SET act_id = LAST_INSERT_ID();
	
	ELSEIF EXISTS (SELECT 1 FROM actor WHERE id_actor = act_id
      		AND (passport_number <> ac_passport_number
           	OR education <> ac_education
           	OR work_experience <> ac_work_experience)
		) THEN
		     UPDATE actor
		     SET passport_number = ac_passport_number, education = ac_education, 
			work_experience = ac_work_experience WHERE id_actor = act_id;
	END IF;
	


	SELECT id_director INTO dir_id
	FROM director
	WHERE surname = d_surname AND name = d_name AND date_of_birth = d_date_of_birth;

	IF dir_id IS NULL THEN
		INSERT INTO director(surname, name, date_of_birth, passport_number, awards)
			VALUES(d_surname, d_name, d_date_of_birth, d_passport_number, d_awards);
		SET dir_id = LAST_INSERT_ID();
	ELSEIF EXISTS (SELECT 1 FROM director WHERE id_director = dir_id
      		AND (passport_number <> d_passport_number
           	OR awards <> d_awards)
		) THEN
		     UPDATE director
		     SET passport_number = d_passport_number, awards = d_awards 
			WHERE id_director = dir_id;
	END IF;

	
	INSERT INTO application(filmography, photos, id_actor, id_role, id_casting_director,
				id_director)
		VALUES(NULL, NULL, act_id, id_input_role, id_cas_dir, dir_id);

END //

DELIMITER ;