SELECT s.name, s.straat, s.huisnr, s.postcode, pc.lat, pc.lng
FROM mhl_suppliers AS s
INNER JOIN pc_lat_long AS pc
ON s.postcode = pc.pc6
ORDER BY lat DESC LIMIT 5;