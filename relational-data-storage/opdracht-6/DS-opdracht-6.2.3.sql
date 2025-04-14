SELECT 
	joindate,
    DAYNAME(joindate) AS dag,
    COUNT(id)
FROM mhl_suppliers
GROUP BY dag
ORDER BY DAYOFWEEK(joindate)