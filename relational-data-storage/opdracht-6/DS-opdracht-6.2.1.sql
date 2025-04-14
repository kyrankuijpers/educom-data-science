SELECT
	name,
    DATE_FORMAT(joindate, "%e-%m-%Y"),
    id
FROM mhl_suppliers
WHERE DAY(joindate) > (DAY(LAST_DAY(joindate)) - 7) 
ORDER BY joindate DESC