SELECT s.name, s.straat, s.huisnr, s.postcode, pt.name
FROM mhl_suppliers AS s
INNER JOIN mhl_yn_properties AS yn 
ON s.id = yn.supplier_ID
INNER JOIN mhl_propertytypes AS pt
ON yn.propertytype_ID = pt.id
WHERE pt.name = "ook voor particulieren" OR pt.name = "specialistische leverancier"
