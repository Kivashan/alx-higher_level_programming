-- a script that displays the top 3 of cities temperature
-- during July and August ordered by temperature (descending)
SELECT DISTINCT city, AVG(value) OVER(PARTITION by city) AS avg_temp
FROM temperatures
WHERE month = 7 OR month = 8
ORDER BY avg_temp DESC LIMIT 3;
