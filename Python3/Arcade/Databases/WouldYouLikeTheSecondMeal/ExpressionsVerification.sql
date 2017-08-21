/*Please add ; after each select statement*/
CREATE PROCEDURE expressionsVerification()
BEGIN
    SELECT *
    FROM expressions
    WHERE operation = "+" and a + b = c
        OR operation = "-" and a - b = c
        OR operation = "/" and a / b = c
        OR operation = "*" and a * b = c;
END
