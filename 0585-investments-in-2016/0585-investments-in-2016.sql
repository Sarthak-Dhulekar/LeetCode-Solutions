WITH COUNTED AS (SELECT
	pid,
    tiv_2016,
    COUNT(*) OVER(PARTITION BY tiv_2015) AS similer,
    COUNT(*) OVER(PARTITION BY lat, lon) AS boths
FROM Insurance)
SELECT
	ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM COUNTED 
WHERE similer > 1 AND boths = 1;