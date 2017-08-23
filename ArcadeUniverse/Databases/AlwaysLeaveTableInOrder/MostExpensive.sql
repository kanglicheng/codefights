/*Please add ; after each select statement*/
CREATE PROCEDURE mostExpensive()
BEGIN
    SELECT name
    FROM Products
    ORDER BY quantity * price DESC, name ASC
    LIMIT 1;
END
