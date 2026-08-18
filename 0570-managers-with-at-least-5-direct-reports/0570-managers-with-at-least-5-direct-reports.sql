WITH manager AS
(SELECT
	DISTINCT managerId,
	COUNT(managerId)
FROM Employee
GROUP BY managerId
HAVING COUNT(managerId) >=5)
SELECT name FROM manager
INNER JOIN
Employee
ON manager.managerId = Employee.id;