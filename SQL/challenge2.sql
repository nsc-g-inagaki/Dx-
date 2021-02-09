SELECT
  continent  AS 大陸名
  ,name AS 国名
  ,surface_area AS 面積
FROM
(
  SELECT
    continent
    ,name
    ,surface_area
    ,rank() over (partition by continent order by surface_area desc)
  FROM country
)
AS challenge2
WHERE rank <= 5
