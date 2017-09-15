/*Please add ; after each select statement*/
CREATE PROCEDURE marketReport()
BEGIN
    SELECT country, COUNT(country) AS competitors
    FROM foreignCompetitors
    GROUP BY country
    UNION ALL
    SELECT "Total:" country, COUNT(competitor)
    FROM foreignCompetitors;
END
