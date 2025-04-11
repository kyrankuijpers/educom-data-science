SELECT 
	c.name AS City,
    COUNT(IF(m.name = 'Bronze', 1, NULL)) AS Bronze,
	COUNT(IF(m.name = 'Silver', 1, NULL)) AS Silver,
	COUNT(IF(m.name = 'Gold', 1, NULL)) AS Gold,
	COUNT(IF(m.name NOT IN ('Gold', 'Silver', 'Bronze'), 1, NULL)) AS Other
FROM mhl_suppliers AS s
LEFT JOIN mhl_cities AS c ON s.city_ID = c.id
LEFT JOIN mhl_membertypes AS m on s.membertype = m.id
GROUP BY c.name
ORDER BY Gold DESC, Silver DESC, Bronze DESC;