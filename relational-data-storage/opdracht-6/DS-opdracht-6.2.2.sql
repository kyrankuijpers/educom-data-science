SELECT
	id,
    joindate,
    DATEDIFF(CURDATE(), joindate) AS dagen_lid
FROM mhl_suppliers
ORDER BY dagen_lid