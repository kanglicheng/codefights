/*Please add ; after each select statement*/
CREATE PROCEDURE projectsTeam()
BEGIN
	SELECT name
    FROM projectLog
    GROUP BY name
    ORDER BY name ASC;
END
