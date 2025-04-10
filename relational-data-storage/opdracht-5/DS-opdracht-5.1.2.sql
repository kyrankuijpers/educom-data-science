SELECT
	year,
    COUNT(hitcount),
    MIN(hitcount),
    MAX(hitcount),
    AVG(hitcount),
    SUM(hitcount)
FROM mhl_hitcount
GROUP BY year;