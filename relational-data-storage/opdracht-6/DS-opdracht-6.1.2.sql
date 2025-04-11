SELECT a.gemeente, b.leverancier, b.total_hitcount, a.average_hitcount
FROM (
    SELECT g.id, l.name AS leverancier, SUM(h.hitcount) AS total_hitcount
  FROM mhl_suppliers l
  INNER JOIN mhl_cities p ON l.city_ID=p.id
  INNER JOIN mhl_communes g ON p.commune_ID=g.id
  INNER JOIN mhl_hitcount h ON h.supplier_ID=l.id
  )
 AS b
INNER JOIN (
    SELECT g.id, AVG(h.hitcount) AS average_hitcount, g.name AS gemeente
    FROM mhl_hitcount h
    INNER JOIN mhl_suppliers l ON h.supplier_ID=l.id
    INNER JOIN mhl_cities p ON l.city_ID=p.id
    INNER JOIN mhl_communes g ON p.commune_ID=g.id
    GROUP BY g.id
    ) AS a ON a.id=b.id
GROUP BY a.id, b.leverancier
HAVING b.total_hitcount > a.average_hitcount
ORDER BY a.gemeente, (b.total_hitcount-a.average_hitcount) DESC