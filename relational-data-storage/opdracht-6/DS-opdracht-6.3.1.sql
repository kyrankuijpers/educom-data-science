SELECT 
	name,
    CONCAT(UPPER(LEFT(name, 1)),     SUBSTRING(name, 2)) AS nicename
FROM mhl_suppliers