-- a script that displays the max temperature
-- of each state (ordered by State name).
SELECT DISTINCT state, MAX(value) OVER(PARTITION BY state) AS max_temp
FROM temperatures
ORDER BY state LIMIT 3;
