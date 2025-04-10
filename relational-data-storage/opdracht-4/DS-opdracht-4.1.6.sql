SELECT hitcount, s.name, cit.name, com.name, dis.name
FROM mhl_hitcount as hit
INNER JOIN mhl_suppliers as s
ON hit.supplier_ID = s.id
INNER JOIN mhl_cities as cit
ON s.city_ID = cit.id
INNER JOIN mhl_communes as com
ON cit.commune_ID = com.id
INNER JOIN mhl_districts as dis
ON com.district_ID = dis.id
WHERE year = 2014 AND month = 1 AND dis.name IN ('Zeeland', 'Limburg', 'Noord-Brabant');