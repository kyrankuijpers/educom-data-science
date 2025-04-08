SELECT s.name, s.straat, s.huisnr, s.postcode, cit.name AS plaatsnaam
FROM mhl_suppliers AS s
INNER JOIN mhl_cities AS cit
ON s.city_ID = cit.id 
INNER JOIN mhl_communes AS com
ON cit.commune_ID = com.id
AND com.name = "Steenwijkerland";
