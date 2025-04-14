SELECT 
    IF(parent.name IS NULL, child.name, CONCAT(parent.name, ' - ', child.name)) AS rubriek,
    IF(ISNULL(SUM(hitcount)), 'Geen hits', SUM(hitcount)) 
FROM mhl_rubrieken AS child
LEFT JOIN mhl_rubrieken AS parent ON child.parent = parent.id
LEFT JOIN mhl_suppliers_mhl_rubriek_view AS sr ON child.id = sr.mhl_rubriek_view_ID
LEFT JOIN mhl_suppliers AS s ON sr.mhl_suppliers_ID = s.id
LEFT JOIN mhl_hitcount AS h ON s.id = h.supplier_ID
WHERE child.name IS NOT NULL
GROUP BY child.id
ORDER BY rubriek
 
