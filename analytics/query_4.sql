#Part 1
#We need to join table based on max timestamp and min timestamp of the user browsed site

SELECT  distinct user_id, max(ts) as maxTime FROM  mytable GROUP BY  user_id
UNION
SELECT  distinct user_id, min(ts) as minTime FROM  mytable GROUP BY  user_id;


#Part 2
#The dataset has duplicates and need to have unique entry per timestamp for
#Final inner joins the site_id with the user_id with
#site on max_time is same as site on min_time


#Query at the end should be
select tbl1.site_id, count(*) from
(SELECT user_id, max(ts) as maxTime FROM  mytable GROUP BY  user_id) as tbl1,
(SELECT user_id, min(ts) as minTime FROM  mytable GROUP BY  user_id) as tbl2
where tbl1.user_id = tbl2.user_id
group by tbl1.site_id
order by count(*) desc;