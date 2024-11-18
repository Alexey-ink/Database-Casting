CREATE TABLE IF NOT EXISTS actor (
    id_actor INT UNSIGNED NOT NULL AUTO_INCREMENT,
    surname varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    name varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    patronymic varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    date_of_birth DATE DEFAULT NULL,
    passport_number VARCHAR(10) DEFAULT NULL,
    education TEXT COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    work_experience TEXT COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    PRIMARY KEY (id_actor)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci AUTO_INCREMENT=1 ;


CREATE TABLE IF NOT EXISTS application (
    id_application INT UNSIGNED NOT NULL AUTO_INCREMENT,
    filmography TEXT COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    photos VARCHAR(200) DEFAULT NULL,
    id_actor INT UNSIGNED NOT NULL, 
    id_role INT UNSIGNED NOT NULL,
    id_сasting_director INT UNSIGNED NOT NULL,
    id_director INT UNSIGNED NOT NULL,
    PRIMARY KEY (id_application),
    FOREIGN KEY (id_actor) REFERENCES actor(id_actor), 
    FOREIGN KEY (id_role) REFERENCES role(id_role),
    FOREIGN KEY(id_сasting_director) REFERENCES casting_director(id_casting_director),
    FOREIGN KEY(id_director) REFERENCES director(id_director)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci AUTO_INCREMENT=1 ;


CREATE TABLE IF NOT EXISTS director(
    id_director INT UNSIGNED NOT NULL AUTO_INCREMENT,
    surname varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    name varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    patronymic varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    date_of_birth DATE DEFAULT NULL,
    passport_number VARCHAR(10) DEFAULT NULL,
    filmography TEXT COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    PRIMARY KEY (id_director)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci AUTO_INCREMENT=1;


CREATE TABLE IF NOT EXISTS casting_director (
    id_casting_director INT UNSIGNED NOT NULL AUTO_INCREMENT,
    surname varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    name varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    patronymic varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    date_of_birth DATE DEFAULT NULL,
    passport_number VARCHAR(10) DEFAULT NULL,
    filmography TEXT COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    PRIMARY KEY (id_casting_director)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci AUTO_INCREMENT=1;

CREATE TABLE IF NOT EXISTS role (
    id_role INT UNSIGNED NOT NULL AUTO_INCREMENT,
    name varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    discription TEXT COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    id_role_type INT UNSIGNED  NOT NULL, 
    id_film INT UNSIGNED  NOT NULL, 
    FOREIGN KEY(id_role_type) REFERENCES role_type(id_role_type),
    FOREIGN KEY(id_film) REFERENCES film(id_film), 
    PRIMARY KEY (id_role)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci AUTO_INCREMENT=1 ;

CREATE TABLE IF NOT EXISTS role_type (
    id_role_type INT UNSIGNED NOT NULL AUTO_INCREMENT,
    name varchar(15) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    PRIMARY KEY (id_role_type)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci AUTO_INCREMENT=1 ;	

CREATE TABLE IF NOT EXISTS film (
    id_film INT UNSIGNED NOT NULL AUTO_INCREMENT,
    name varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    id_director INT UNSIGNED  NOT NULL, 
    id_casting_director INT UNSIGNED NOT NULL,
    FOREIGN KEY(id_director) REFERENCES director(id_director),
    FOREIGN KEY(id_casting_director) REFERENCES casting_director(id_casting_director), 
    PRIMARY KEY (id_film)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci AUTO_INCREMENT=1 ;


CREATE TABLE IF NOT EXISTS film_genres (
    id_film_genres INT UNSIGNED NOT NULL AUTO_INCREMENT,
    PRIMARY KEY (id_film_genres),
    id_film INT UNSIGNED NOT NULL,
    id_genres INT UNSIGNED NOT NULL,
    FOREIGN KEY(id_film) REFERENCES film(id_film), 
    FOREIGN KEY(id_genres) REFERENCES genres(id_genres) 
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci AUTO_INCREMENT=1 ;

CREATE TABLE IF NOT EXISTS genres (
    id_genres INT UNSIGNED NOT NULL AUTO_INCREMENT,
    name VARCHAR(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    PRIMARY KEY (id_genres)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci AUTO_INCREMENT=1 ;


CREATE TABLE IF NOT EXISTS first_stage (
    id_first_stage INT UNSIGNED NOT NULL AUTO_INCREMENT,
    directors_assessment TINYINT UNSIGNED DEFAULT NULL, 
    casting_directors_assesment TINYINT UNSIGNED DEFAULT NULL,
    id_application INT UNSIGNED NOT NULL,  
    PRIMARY KEY (id_first_stage),
    FOREIGN KEY(id_application) REFERENCES application(id_application) 
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci AUTO_INCREMENT=1 ;


CREATE TABLE IF NOT EXISTS audition (
    id_audition INT UNSIGNED NOT NULL AUTO_INCREMENT,
    directors_assessment TINYINT UNSIGNED DEFAULT NULL, 
    casting_directors_assesment TINYINT UNSIGNED DEFAULT NULL,
    id_application INT UNSIGNED NOT NULL,  
    PRIMARY KEY (id_audition),
    FOREIGN KEY(id_application) REFERENCES application(id_application) 
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci AUTO_INCREMENT=1 ;

CREATE TABLE IF NOT EXISTS doubles_audition (
    id_doubles_audition INT UNSIGNED NOT NULL AUTO_INCREMENT,
    directors_assessment TINYINT UNSIGNED DEFAULT NULL, 
    casting_directors_assesment TINYINT UNSIGNED DEFAULT NULL,
    id_application INT UNSIGNED NOT NULL,
    results SMALLINT UNSIGNED DEFAULT NULL,
    getting_a_role VARCHAR(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    PRIMARY KEY (id_doubles_audition),
    FOREIGN KEY(id_application) REFERENCES application(id_application)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci AUTO_INCREMENT=1 ;








