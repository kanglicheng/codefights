/*Please add ; after each select statement*/
CREATE PROCEDURE securityBreach()
BEGIN
    SELECT first_name, second_name, attribute
    FROM users
    WHERE attribute LIKE CONCAT(
        "%_\%",
        BINARY first_name,
        "\_",
        BINARY second_name,
        "\%%"
    )
    ORDER BY attribute;
END
