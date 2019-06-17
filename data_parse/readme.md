# Moloco online assessment question-2
Problem Statement:
Using one of the languages from {Go, Python, Java, C++}, implement a function/method that computes the most popular product(s) according to two different measures.
Implement this function/method and submit a link to your code (answer) below.
You can share via a link to your code using free websites like https://gist.github.com/ or ideone.com.

You are given a text file where each line contains a JSON message as string, containing three fields: user_id (string), product_id (string), and quantity (integer). You can assume that each line is a valid JSON message. 

For instance, a text file may contain the following three lines:
{"user_id" : "uid_1", "product_id" : "pid_1", "quantity" : 45}
{"user_id" : "uid_1", "product_id" : "pid_2", "quantity" : 1}
{"user_id" : "uid_2", "product_id" : "pid_2", "quantity" : 5}

Given this as input (assume that it is a text file stored in your local machine), write a program that reads the file, and computes the most popular products based on two ranking methods.

(1) Based on the unique number of users who purchased each product, and
(2) Based on the total quantity of each product sold.

For instance, using the above example with 3 data points, the most popular product based on ranking method #1 is "pid_2" because it was purchased by two different users (where as "pid_1" was purchased only by one user).
On the other hand, using ranking method #2, "pid_1" is the winner as 45 units of "pid_1" was sold whereas only 1+5=6 units of "pid_2" was sold.

In case of ties, your program must output the product ids that are tied.
The output can be simply printed to the console in a human-readable manner. 
Refer to the sample output message below.

Sample Output:
Most popular product(s) based on the number of purchasers: [ "pid_2" ]
Most popular product(s) based on the quantity of goods sold: [ "pid_1" ]

For testing purposes, you can download a sample input file from here, and run your program:
https://docs.google.com/spreadsheets/d/1dYKJFZkZ-qTcQOrbf80u85Zl1ugrRly3p_AJaQixgcw/edit#gid=1692443255
(You can download this as a CSV/TSV file or you can simply copy-and-paste the contents.
The sheet contains 2,373 rows.)

Constraints:
You can assume that the input file is fairly small in size (less than 1M lines).
user_id and product_id are both strings of length at most 10.
quantity is a positive integer between 1 and 100.
Each line is a valid JSON message and always contains three elements (user_id, product_id, and quantity).


1.Run file rank_product.py to get the required o/p of the 
two ranking problems

2.Dabatabse is extracted in a separate function defined in database class 
in database.py file in order to  maintain single responsility of the code

3.Json parsing into dictionary is handled separately,
in the file json_load.py
