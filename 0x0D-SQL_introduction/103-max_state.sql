-- display max temp
SELECT `state`, MAX(`value`) AS `max_temp`
FROM `temperatues`
GROUP BY `state`
ORDER BY `state`;
