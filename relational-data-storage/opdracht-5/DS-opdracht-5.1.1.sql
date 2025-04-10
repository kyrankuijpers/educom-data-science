SELECT 
	COUNT(hitcount) AS 'aantal records', 
    MIN(hitcount) AS 'minimum', 
    MAX(hitcount) AS 'maximum',  
    AVG(hitcount) AS 'gemiddelde',
    SUM(hitcount) AS 'totaal'
FROM mhl_hitcount;