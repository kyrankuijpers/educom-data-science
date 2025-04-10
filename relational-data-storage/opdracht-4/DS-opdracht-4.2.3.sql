SELECT   
	R.id,
	IF(ISNULL(PR.name), R.name, PR.name) AS hoofdrubriek,     
    IF(ISNULL(PR.name), '', R.name) AS subrubriek 
FROM mhl_rubrieken AS R 
LEFT JOIN mhl_rubrieken AS PR ON R.parent = PR.id 
ORDER BY hoofdrubriek, subrubriek;
