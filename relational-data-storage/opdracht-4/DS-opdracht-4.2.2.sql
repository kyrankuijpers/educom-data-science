SELECT 
	cit.name AS plaatsnaam,
    IF(com.name IS NULL, 'INVALID', com.name) AS gemeentenaam
FROM mhl_cities AS cit
LEFT JOIN mhl_communes AS com ON cit.commune_ID = com.id;
