WITH Rank_temp AS (
    SELECT 
        id,
        temperature,
        recordDate,
        LAG(temperature) OVER (ORDER BY recordDate) AS prev_temperature,
        LAG(recordDate) OVER (ORDER BY recordDate) AS prev_date
    FROM Weather
)
SELECT id AS Id
FROM Rank_temp
WHERE temperature > prev_temperature
  AND DATEDIFF(recordDate, prev_date) = 1;