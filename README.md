# FSND-Log-Analysis-Project


This project in Udacity's Connect Full Stack Web Developer. 
It is about creating a reporting tool that prints out reports based on the data in the database. 
This reporting tool is a Python program using the psycopg2 module to connect to the database.

## Getting Started

The questions the reporting tool should answer with these outputs:		
```
1. What are the most popular three articles of all time?

Most popular three articles of all time:
- Candidate is jerk, alleges rival -- 338647 views
- Bears love berries, alleges bear -- 253801 views
- Bad things gone, say good people -- 170098 views

2. Who are the most popular article authors of all time?

Most popular article authors of all time:
- Ursula La Multa -- 507594 views
- Rudolf von Treppenwitz -- 423457 views
- Anonymous Contributor -- 170098 views

3. On which days did more than 1% of requests lead to errors?

Days with more than 1% of error requests:
Jul 17,2016 -- 2.26% errors
```

### Installing
 
- Install vagrant
- Install virtual machine
- In terminal
```
vagrant up
vagrant ssh
cd /vagrant
```
- Download a FSND virtual machine: https://github.com/udacity/fullstack-nanodegree-vm
- Download data: https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
- To load the data use the command 
```
cd /vagrant psql -d news -f newsdata.sql
```
- To run project use this command
```
cd /vagrant/projectfolder python3 log-analysis-project.py
```
### Result

After run the project you can check the output in OUTPUT.txt.
