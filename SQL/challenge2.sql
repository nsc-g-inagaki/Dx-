SELECT continent AS 大陸名,name AS 国名,surface_area AS 面積
FROM (

    SELECT continent,name,surface_area
    ,ROW_NUMBER() OVER (PARTITION BY continent ORDER BY surface_area desc)
    FROM country)AS rank

WHERE ROW_NUMBER <= 5;