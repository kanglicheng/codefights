/*Please add ; after each select statement*/
CREATE PROCEDURE suspectsInvestigation()
BEGIN
	SELECT id, name, surname
    FROM Suspect
    WHERE height <= 170
        AND LENGTH(surname) = 5
        AND LEFT(LOWER(name), 1) = "b"
        AND LOWER(surname) LIKE "gre_n";
END
