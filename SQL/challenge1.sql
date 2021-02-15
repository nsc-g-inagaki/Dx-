SELECT T1.continent AS 大陸名,T1.code AS 国コード,T1.name AS 国名,
T1.local_name AS 国名（読み方）,T2.name AS 首都,T3.language AS 標準語
FROM country AS T1
JOIN city AS T2 
ON T1.capital =T2.id
JOIN country_language AS T3
ON T1.code  = T3.country_code
WHERE is_official = true
ORDER BY T1.continent ASC,T1.code ASC,T1.name ASC;