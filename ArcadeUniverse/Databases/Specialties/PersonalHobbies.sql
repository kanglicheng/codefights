/*Please add ; after each select statement*/
CREATE PROCEDURE personalHobbies()
BEGIN
    SELECT name
    FROM people_hobbies
    WHERE FIND_IN_SET("sports", hobbies) AND FIND_IN_SET("reading", hobbies)
    ORDER BY name;
END
