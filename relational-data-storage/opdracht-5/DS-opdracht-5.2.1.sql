SELECT 
	s.name AS leverancier,
    IF(NOT ISNULL(con.name) AND con.department = 3, con.name, 'tav directie') AS aanhef,
    IF (p_address<>'', p_address, CONCAT(straat, ' ', huisnr)) AS adres,
    IF (p_address<>'', p_postcode, postcode) AS postcode,
    IF (p_address<>'', cit1.name, cit2.name) AS stad,
    IF (p_address<>'', d1.name, d2.name) AS provincie
FROM mhl_suppliers AS s
LEFT JOIN mhl_cities AS cit1 ON cit1.id=s.p_city_ID
LEFT JOIN mhl_communes AS com1 ON com1.id=cit1.commune_ID
LEFT JOIN mhl_districts AS d1 ON d1.id=com1.district_ID
LEFT JOIN mhl_cities AS cit2 ON cit2.id=s.city_ID
LEFT JOIN mhl_communes AS com2 ON com2.id=cit2.commune_ID
LEFT JOIN mhl_districts AS d2 ON d2.id=com2.district_ID
LEFT JOIN mhl_contacts AS con ON s.id = con.supplier_ID AND con.department=3
WHERE s.postcode <> ''
ORDER BY provincie, stad, s.name;  
