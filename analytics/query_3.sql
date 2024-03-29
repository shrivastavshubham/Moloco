#Answer could be incorrect  as the dataset should have 1 row per timestamp per user
#if it would have been like mentioned then the query should be:
#The order of the result still should be correct

SELECT f.site_id,count(*) AS cnt
FROM (SELECT max(ts) as ts1, user_id
FROM  mytable
GROUP BY user_id
) AS x INNER JOIN mytable AS f on f.user_id = x.user_id AND f.ts = x.ts1
GROUP BY f.site_id ORDER BY cnt DESC limit 3;