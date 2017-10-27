/*Please add ; after each select statement*/
CREATE PROCEDURE orderingEmails()
BEGIN
    SELECT id, email_title,
        (IF(FLOOR(size / 1024) < 1024,
            CONCAT(FLOOR(size / 1024), " Kb"),
            CONCAT(FLOOR(size / (1024 * 1024)), " Mb"))) as short_size
    FROM emails
    ORDER BY size DESC;
END
