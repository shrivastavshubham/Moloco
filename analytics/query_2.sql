select user_id, site_id, count(*) as cnt
from mytable
WHERE ts BETWEEN '2019-02-03 00:00:00' and '2019-02-04 23:59:59'
group by 1, 2
HAVING count(*) > 10
ORDER BY cnt DESC;