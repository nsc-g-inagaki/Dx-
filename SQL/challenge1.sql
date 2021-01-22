--challenge1.sql

select
 country.continent AS 大陸名,
 country.code AS 国コード,
 country.name AS 国名,
 country.local_name AS 国名（読み方）,
 city.name AS 首都,
 country_language.language AS 標準語

from country_language
inner join country on country.code = country_language.country_code
inner join city on country.capital = city.id

where
 country_language.is_official is true

ORDER BY
 country.continent ASC,
 country.code ASC,
 country.name ASC
;