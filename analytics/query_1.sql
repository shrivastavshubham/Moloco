select count(*) as count, site_id
from (select distinct user_id, site_id
      from mytable
      Where country_id='BDV'
     ) et GROUP BY site_id ORDER BY count DESC limit 1;