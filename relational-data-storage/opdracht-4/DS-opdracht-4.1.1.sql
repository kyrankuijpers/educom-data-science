SELECT s.name, s.straat, s.huisnr, s.postcode 
FROM mhl_suppliers AS s
INNER JOIN mhl_cities as c
ON s.city_ID = c.id 
AND c.name = 'Amsterdam';
