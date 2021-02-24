select *
from
 (
   select
   ROW_NUMBER() over (partition by country.continent order by surface_area desc) as rank
  ,continent AS "大陸名"
  ,name AS "国名"
  ,surface_area AS "面積"
   from
   country
 ) AS "area_rank"
where area_rank.rank <= 5