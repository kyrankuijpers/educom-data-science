SELECT 
	s.name,
	IF(NOT ISNULL(d.contact), d.contact, 'tav directie') AS aanhef,
    v.adres,
    v.postcode,
    v.stad
FROM v_verzendlijst AS v
LEFT JOIN v_directie AS d ON v.id = d.id 
LEFT JOIN mhl_suppliers AS s ON v.id = s.id
WHERE (NOT ISNULL(s.name))
ORDER BY s.name