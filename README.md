# Log Analysis

The Log Analysis is the third project of Udacity Full Stack Nano Degree Program. Log Analysis is a reporting tool that will use information from the database to discover what kind of articles the site's readers like. The database contains newspaper articles, as well as the web server log for the site.

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
create view popular_authors as
select articles.author, articles.slug as article, count(*) as views
from log, articles where log.path like(concat('/article/',articles.slug))
group by article, author order by views desc;

### create view total_req
create view total_req as
select count(*) as count, date(time) as date from log
group by date order by count desc;

### create view err_req
create view err_req as select count(*)
as count, date(time) as date from log where status != '200 OK'
group by date order by count desc;

### create view error_per
create view error_per as
select total_req.date, round((100.0*err_req.count)/total_req.count,2)as err_persent
from err_req, total_req where err_req.date = total_req.date;
