SELECT S.name, PT.name, IF(ISNULL(YN.content), 'NOT SET', YN.content) AS value
FROM mhl_propertytypes AS PT
CROSS JOIN mhl_suppliers AS S
LEFT JOIN mhl_yn_properties AS YN
ON PT.id = YN.propertytype_ID AND YN.supplier_ID = S.id
INNER JOIN mhl_cities AS C
ON S.city_ID = C.id
WHERE C.name = "Amsterdam" AND PT.proptype = "A";