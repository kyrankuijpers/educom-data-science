SELECT s.name, straat, huisnr, postcode, r.name as R_rubriek, pr.name as PR_rubriek
FROM mhl_suppliers AS s
INNER JOIN mhl_cities AS c ON s.city_ID = c.id
INNER JOIN mhl_suppliers_mhl_rubriek_view AS sr ON s.id = sr.mhl_suppliers_ID
INNER JOIN mhl_rubrieken AS r ON sr.mhl_rubriek_view_ID = r.id
LEFT JOIN mhl_rubrieken AS pr ON r.parent = pr.id
WHERE c.name = 'Amsterdam' AND (pr.name = 'drank' OR r.name = 'drank')
ORDER BY r.name, s.name;
