SELECT name, straat, huisnr, postcode 
FROM mhl_suppliers 
WHERE (city_ID = (SELECT id FROM mhl_cities WHERE name = 'Amsterdam') 
AND NOT(p_city_ID = (SELECT id FROM mhl_cities WHERE name = 'Amsterdam')));