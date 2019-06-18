# Question 3
Problem Statement:

"Suppose you have time-series data consisting of (timestamp, user_id, country_id, site_id).
Each entry (row) is created when a user (of user_id) from some country (country_id) visited a certain website (site_id) at a certain time (timestamp).
We want to analyze this data.
You can find the data here:
https://docs.google.com/spreadsheets/d/1dYKJFZkZ-qTcQOrbf80u85Zl1ugrRly3p_AJaQixgcw/edit#gid=1910446069

For instance, in row 2 you will see the following row:
"2019-02-01 00:01:24	LC36FC	TL6	N0OTG"
This tells us that at "2019-02-01 00:01:24" user "LC36FC" from country "TL6" visited website "N0OTG".

The sheet contains 3554 rows (including the header) and four columns (ts for timestamp, user_id, country_id, site_id).

Using any programming/query language and free/commercial tools you like, answer the following questions. 
At the end, briefly describe how you computed the answers (and provide a link to code if any)."


Part-1

544	5NPAU

Part-2

LC3A59	N0OTG	26
LC06C3	N0OTG	25
LC3C9D	N0OTG	17
LC3C7E	3POLC	15

Part-3

Incorrect ans (as dups in dataset for same timestamp,user,site,country)
1043	5NPAU
564	N0OTG
296	QGO3G

Part-4

Didn't get the answer as dups in dataset (mentioned before)

If the dataset would have had unique rows it would have,
been possible (easier) to query using mysql.
The possible query is present in the query(sql) files.
The problem could be solved using in any programming language,
but the code could be messy.

Decided to solve in Mysql because the problem had
inputs to support it.

