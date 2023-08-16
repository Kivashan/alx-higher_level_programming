-- a script that displays the average temperature (Fahrenheit)
-- by city ordered by temperature (descending).
SELECT DISTINCT city, AVG(value) OVER(PARTITION BY city) AS avg_temp
FROM temperatures
ORDER BY avg_temp DESC;
