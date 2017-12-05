CREATE VIEW total_req AS
SELECT COUNT(*) AS count,
DATE(time) AS date
FROM log
GROUP BY date
ORDER BY count DESC;

CREATE VIEW err_req
AS SELECT
COUNT(*) as count,
DATE(time) AS date
FROM log
WHERE status != '200 OK'
GROUP BY date
ORDER BY count DESC;

CREATE VIEW error_per
AS SELECT total_req.date,
ROUND((100.0*err_req.count)/total_req.count,2)AS err_persent
FROM err_req, total_req
WHERE err_req.date = total_req.date;

CREATE VIEW popular_authors
AS SELECT articles.author, articles.title AS article,
COUNT(*) AS views
FROM log, articles
WHERE log.path = (concat('/article/',articles.slug))
GROUP BY article, author
ORDER BY views DESC;
