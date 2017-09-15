/*Please add ; after each select statement*/
CREATE PROCEDURE nullIntern()
BEGIN
    SELECT COUNT(*) AS number_of_nulls
    FROM departments
    WHERE (description IS NULL
        or TRIM(LOWER(description)) LIKE "null"
        or TRIM(LOWER(description)) LIKE "-"
        or TRIM(LOWER(description)) LIKE "nil");
END
