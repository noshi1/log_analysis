#!/usr/bin/env python3

import psycopg2
from psycopg2 import Error

DBNAME = "news"

# 1. What are the most popular three articles of all time?
query1 = """Select articles.title AS article, count(*) AS views
            FROM log, articles
            WHERE log.path = (concat('/article/',articles.slug))
            GROUP BY article
            ORDER BY views DESC
            LIMIT 3;
            """

# 2. Who are the most popular article authors of all time?
query2 = "select name, sum(views) as views from authors,\
popular_authors where authors.id = popular_authors.author\
 group by name order by views desc;"

# 3. On which days did more than 1% of requests lead to errors?
query3 = "select * from error_per where err_persent > 1.0;"

def create_conn(query):
    """Connect to PostgreSQL databse and returns a database connection."""
    try:
        conn = psycopg2.connect(database=DBNAME)
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except:
        print("Unable to connect to the database")

def popular_articles(query1):
    """ This method will return top three popular articles."""
    result = create_conn(query1)
    print("Popular articles:")
    for i, (article, view) in enumerate(result, 1):
        article_view = "{}. {} -- {} views".format(i, article, view)
        print(article_view)
    
def popular_authors(query):
    """This method will print top most popular article authors."""
    print("Popular authors:")
    for row in range(len(result)):
        author = result[row][0]
        view = result[row][1]
        author_view = "{}. {} -- {} views".format(row+1, author, view)
        print(author_view)

    conn.close()

def log_error(query):
    """This method will print which days more requests goes to errors."""
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
