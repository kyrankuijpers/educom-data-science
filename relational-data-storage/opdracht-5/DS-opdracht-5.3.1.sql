CREATE VIEW v_DIRECTIE AS
	SELECT 
		supplier_ID AS id,
		c.name AS contact,
		contacttype AS functie,
		d.name AS department
	FROM mhl_contacts AS c
	LEFT JOIN mhl_departments AS d ON c.department = d.id
	WHERE (d.name = 'directie' OR contacttype LIKE '%directeur%')
	ORDER BY supplier_ID