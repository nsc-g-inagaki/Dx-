SELECT
continent AS "大陸名", code AS "国コード", country.name AS "国名", local_name AS "国名（読み方）", city.name AS "首都", language AS "標準語"
FROM
country
JOIN
city
ON
code = city.country_code
RIGHT JOIN
country_language
ON
code = country_language.country_code
ORDER BY continent ASC, code ASC, country.name ASC;
