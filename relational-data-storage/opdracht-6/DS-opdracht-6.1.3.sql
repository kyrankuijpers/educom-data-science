SELECT 
	IF(parent.name IS NULL, child.name, CONCAT(parent.name, ' - ', child.name)) AS rubriek,
    COUNT(s.id)
FROM mhl_rubrieken AS child
LEFT JOIN mhl_rubrieken AS parent ON child.parent = parent.id
INNER JOIN mhl_suppliers_mhl_rubriek_view AS sr ON child.id = sr.mhl_rubriek_view_ID
INNER JOIN mhl_suppliers AS s ON sr.mhl_suppliers_ID = s.id
WHERE child.name IS NOT NULL
GROUP BY rubriek  