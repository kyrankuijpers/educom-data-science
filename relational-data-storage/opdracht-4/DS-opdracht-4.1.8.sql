SELECT 
	cit1.name, 
    cit2.name, 
    cit1.id, 
    cit2.id, 
    cit1.commune_ID, 
    cit2.commune_ID, 
    com1.id, 
    com2.id, 
    com1.name, 
    com2.name
FROM mhl_cities AS cit1
INNER JOIN mhl_cities AS cit2 ON cit1.name = cit2.name
INNER JOIN mhl_communes AS com1 ON cit1.commune_ID = com1.id
INNER JOIN mhl_communes AS com2 ON cit2.commune_ID = com2.id
WHERE cit1.id < cit2.id  AND com1.name IS NOT NULL AND com2.name IS NOT NULL
ORDER BY cit1.name;