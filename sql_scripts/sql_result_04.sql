Select
    neighborhoods.neighborhood_id,
    neighborhoods.name
FROM
    neighborhoods
WHERE
    neighborhoods.name LIKE 'O''Hare' OR neighborhoods.name LIKE 'Loop';