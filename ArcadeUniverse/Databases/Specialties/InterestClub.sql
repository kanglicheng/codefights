CREATE PROCEDURE interestClub()
    SELECT name
    FROM people_interests
    WHERE interests & (LOCATE("drawing", interests)>0) AND interests & (LOCATE("reading", interests)>0)
    ORDER BY name
