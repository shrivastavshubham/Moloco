CREATE TABLE if not exists mytable(
   ts         DATETIME NOT NULL PRIMARY KEY
  ,user_id    VARCHAR(6) NOT NULL
  ,country_id VARCHAR(3) NOT NULL
  ,site_id    VARCHAR(5) NOT NULL
);