SELECT
    YEAR(joindate) AS jaar,
    MONTHNAME(joindate) AS maand,
	COUNT(id)
FROM mhl_suppliers
GROUP BY jaar, maand
ORDER BY jaar, MONTH(joindate)