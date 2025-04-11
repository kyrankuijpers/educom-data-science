CREATE VIEW v_VERZENDLIJST AS 
	SELECT 
		s.id,
		IF(p_address<>'', p_address, CONCAT(straat, ' ', huisnr)) AS adres,
		IF(p_address<>'', p_postcode, s.postcode) AS postcode,
		IF(p_address<>'', cit2.name, cit1.name) AS stad
	FROM mhl_suppliers AS s
	LEFT JOIN pc_lat_long AS pc1 ON s.postcode = pc1.pc6
	LEFT JOIN pc_lat_long AS pc2 ON s.p_postcode = pc2.pc6
	LEFT JOIN mhl_cities AS cit1 ON s.city_ID = cit1.id
	LEFT JOIN mhl_cities AS cit2 ON s.p_city_ID = cit2.id
