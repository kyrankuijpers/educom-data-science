SELECT s.name, SUM(h.hitcount) AS totaal, COUNT(h.month), AVG(h.hitcount) AS gem
FROM mhl_hitcount AS h
INNER JOIN mhl_suppliers AS s
ON h.supplier_ID = s.id
WHERE (NOT supplier_ID = 0)
GROUP BY s.name
HAVING totaal > 100
ORDER BY gem DESC;

