/*Please add ; after each select statement*/
CREATE PROCEDURE itemCounts()
BEGIN
	SELECT item_name, item_type, COUNT(item_name) AS item_count
    FROM availableItems
    GROUP BY item_type ASC, item_name ASC;
END
