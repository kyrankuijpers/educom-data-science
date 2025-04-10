SELECT cit1.name, cit2.name, cit1.id, cit2.id, cit1.commune_ID, cit2.commune_ID
FROM mhl_cities AS cit1
INNER JOIN mhl_cities AS cit2
ON cit1.name = cit2.name
WHERE cit1.id < cit2.id
ORDER BY cit1.name;