DELIMITER //

CREATE FUNCTION GetFullName (
    surname VARCHAR(30), 
    name VARCHAR(20),
    patronymic VARCHAR(20)
) RETURNS VARCHAR(35)
DETERMINISTIC
BEGIN 
    RETURN CONCAT(
        LEFT(name, 1), '.', 
        IF(patronymic IS NOT NULL, CONCAT(LEFT(patronymic, 1), '.'), ''),
        surname
    );
END //

DELIMITER ;