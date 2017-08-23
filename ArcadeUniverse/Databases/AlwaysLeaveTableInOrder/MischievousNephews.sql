/*Please add ; after each select statement*/
CREATE PROCEDURE mischievousNephews()
BEGIN
	SELECT WEEKDAY(mischief_date) as weekday,
        mischief.*
    FROM mischief
    ORDER BY
        weekday,
        FIELD(author, "Huey", "Dewey", "Louie"),
        mischief_date,
        title;
END
