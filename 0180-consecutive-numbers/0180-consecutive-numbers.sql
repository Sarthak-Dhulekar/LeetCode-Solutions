WITH compare AS (SELECT
	num AS col,
    LEAD(num, 1) OVER() AS  column1,
    LEAD(num, 2) OVER() AS column2
FROM Logs)
SELECT
	DISTINCT col AS ConsecutiveNums
FROM compare
WHERE col = column1 AND col = column2;