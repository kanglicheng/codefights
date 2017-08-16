/*Please add ; after each select statement*/
CREATE PROCEDURE suspectsInvestigation2()
BEGIN
	SELECT id, name, surname
    FROM Suspect
    WHERE height <= 170
        OR LENGTH(surname) <> 5
        OR LEFT(LOWER(name), 1) <> "b";
END
