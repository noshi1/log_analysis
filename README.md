# Log Analysis

The Log Analysis is the third project of Udacity Full Stack Nano Degree Program. Log Analysis is a reporting tool that will use information from the database to discover what kind of articles the site's readers like. The database contains newspaper articles, their authors as well as the web server log for the site.

## Tools required to run Log Analysis
* VirtualBox
* Vagrant
* Python3

## Setup

To setup the Virtual machine you need to fork this file:
[virtual machine setup](https://github.com/udacity/fullstack-nanodegree-vm)
unzip this file and cd to this directory from your terminal then cd to vagrant folder.

## To Run
* To startup run **vagrant up**
* To log into Linux VM run **vagrant ssh**

To load the data cd into the vagrant directory and use the command psql -d news -f newsdata.sql.
The database contains these three tables:
* articles
* authors
* log

## PSQL commands to create the database views are:

### create view popular_authors
CREATE VIEW popular_authors
AS SELECT articles.author, articles.title AS article,
COUNT(*) AS views
FROM log, articles
WHERE log.path = (concat('/article/',articles.slug))
GROUP BY article, author
ORDER BY views DESC;

### create view total_req
CRAETE VIEW total_req AS
SELECT COUNT(*) AS count,
DATE(time) AS date
FROM log
GROUP BY date
ORDER BY count DESC;

### create view err_req
CREATE VIEW err_req
AS SELECT
COUNT(*) as count,
DATE(time) AS date
FROM log
WHERE status != '200 OK'
GROUP BY date
ORDER BY count DESC;

### create view error_per
CREATE VIEW error_per
AS SELECT total_req.date,
ROUND((100.0*err_req.count)/total_req.count,2)AS err_persent
FROM err_req, total_req
WHERE err_req.date = total_req.date;
