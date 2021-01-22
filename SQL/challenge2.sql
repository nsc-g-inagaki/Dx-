--challenge2.sql

select
 s.continent AS 大陸名,
 s.name AS 国名,
 s.surface_area AS 面積

from
 (select
   continent,
   name,
   surface_area,
   RANK() OVER(PARTITION BY continent ORDER BY surface_area DESC) AS rank
  from country) AS s

where
 s.rank < 6

ORDER BY
 continent ASC,
 surface_area DESC
;