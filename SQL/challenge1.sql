SELECT
  A.CONTINENT AS 大陸名
  ,A.CODE AS 国コード
  ,A.NAME AS 国名
  ,A.LOCAL_NAME AS 国名（読み方）
  ,B.name AS 首都
  ,C.language AS 標準語
FROM
  country A
INNER JOIN
  city B
  ON A.capital = B.id
INNER JOIN
  country_language C
  ON B.country_code = C.country_code
WHERE
  C.is_official = 'true'
ORDER BY
  A.continent ASC, A.code ASC, A.name ASC
