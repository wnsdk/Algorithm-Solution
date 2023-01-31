SELECT HOUR(DATETIME) AS HOUR, COUNT(*) AS COUNT
FROM ANIMAL_OUTS
GROUP BY HOUR
HAVING 9 <= HOUR AND HOUR < 20
ORDER BY HOUR