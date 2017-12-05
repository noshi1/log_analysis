# Log Analysis

## About
Log Analysis is a reporting tool that will use information from a PostgreSQL database for a fictional news website to discover what kind of articles the site's readers like. The database contains newspaper articles, their authors as well as the web server log for the site. This Log Analysis tool will give us information about:
* What are the most popular three articles of all time?
* Who are the most popular article authors of all time?
* On which days did more than 1% of requests lead to errors?

## Tools required

Download and install all the following softwares:
* [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
* [Vagrant](https://www.vagrantup.com/)
* [Python3](https://www.python.org/downloads/)
When all these tools are installed run these command in your terminal.
* To startup run **vagrant up**
* To log into Linux VM run **vagrant ssh**

## Setup

To setup you need to fork these files:
* [Vagrantfile](https://github.com/noshi1/log_analysis/blob/master/Vagrantfile)
* [newsdata](https://github.com/noshi1/log_analysis/blob/master/newsdata.zip)
Unzip newsdata sql script file. To load the data cd into your directory where all log Analysis project files are and then use the command `psql -d news -f newsdata.sql`.
The database contains these three tables:
* articles
* authors
* log
To import and create views in news database download the following sql script file and run this command `psql -d news -f create_views.sql`
[create_views](https://github.com/noshi1/log_analysis/blob/master/create_views.sql)

## You can also create views in news database manually by running the following sql queries
### create view popular_authors
```sql
CREATE VIEW popular_authors
AS SELECT articles.author, articles.title AS article,
COUNT(*) AS views
FROM log, articles
WHERE log.path = (concat('/article/',articles.slug))
GROUP BY article, author
ORDER BY views DESC;
```

### create view total_req
```sql
CRAETE VIEW total_req AS
SELECT COUNT(*) AS count,
DATE(time) AS date
FROM log
GROUP BY date
ORDER BY count DESC;
```

### create view err_req
```sql
CREATE VIEW err_req
AS SELECT
COUNT(*) as count,
DATE(time) AS date
FROM log
WHERE status != '200 OK'
GROUP BY date
ORDER BY count DESC;
```

### create view error_per
```sql
CREATE VIEW error_per
AS SELECT total_req.date,
ROUND((100.0*err_req.count)/total_req.count,2)AS err_persent
FROM err_req, total_req
WHERE err_req.date = total_req.date;
```

## Execute the program
To execute the program run `python log_analysis.py` or `python3 log_analysis` from your terminal.
