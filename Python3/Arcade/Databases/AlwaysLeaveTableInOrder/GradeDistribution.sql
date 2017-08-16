/*Please add ; after each select statement*/
CREATE PROCEDURE gradeDistribution()
BEGIN
	SELECT Name, ID
    FROM Grades
    WHERE Midterm1 + Midterm2 < Final * 2
    ORDER BY LEFT(Name, 3) ASC, ID ASC;
END
