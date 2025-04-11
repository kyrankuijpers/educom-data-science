SELECT
	year,
    SUM(IF(month BETWEEN 1 AND 3, hitcount, 0)) AS 'Eerste kwartaal',
	SUM(IF(month BETWEEN 4 AND 6, hitcount, 0)) AS 'Tweede kwartaal',
	SUM(IF(month BETWEEN 7 AND 9, hitcount, 0)) AS 'Derde kwartaal',
	SUM(IF(month BETWEEN 10 AND 12, hitcount, 0)) AS 'Vierde kwartaal',
    SUM(hitcount) AS totaal
FROM mhl_hitcount
GROUP BY year
