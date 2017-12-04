# Database code to connect postgresql

import psycopg2
from psycopg2 import Error

DBNAME = "news"

# 1. What are the most popular three articles of all time?
query1 = "select articles.slug as article, count(*) as views from log,\
articles where log.path like(concat('/article/',articles.slug))\
group by article order by views desc limit 3;"

# 2. Who are the most popular article authors of all time?
query2 = "select name, sum(views) as views from authors,\
popular_authors where authors.id = popular_authors.author\
 group by name order by views desc;"

# 3. On which days did more than 1% of requests lead to errors?
query3 = "select * from error_per where err_persent > 1.0;"

# This method will get top three popular articles


def popular_articles(query):
    conn = psycopg2.connect(database=DBNAME)
    cur = conn.cursor()
    cur.execute(query)
    result = cur.fetchall()
    print("Popular articles:")
    for row in range(len(result)):
        article = result[row][0]
        view = result[row][1]
        article_view = "{}. {} -- {} views".format(row+1, article, view)
        print(article_view)

    conn.close()

# This method will print top most popular article authors


def popular_authors(query):
    conn = psycopg2.connect(database=DBNAME)
    cur = conn.cursor()
    cur.execute(query)
    result = cur.fetchall()
    print("Popular authors:")
    for row in range(len(result)):
        author = result[row][0]
        view = result[row][1]
        author_view = "{}. {} -- {} views".format(row+1, author, view)
        print(author_view)

    conn.close()

# This method will print which days more requests goes to errors


def log_error(query):
    conn = psycopg2.connect(database=DBNAME)
    cur = conn.cursor()
    cur.execute(query)
    result = cur.fetchall()
    print("More then 1% error days: ")
    for row in range(len(result)):
        day = result[row][0]
        errors = result[row][1]
        error_days = "{}. {} -- {} errors".format(row+1, day, errors)
        print(error_days)


if __name__ == '__main__':
    popular_articles(query1)
    popular_authors(query2)
    log_error(query3)
