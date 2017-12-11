import psycopg2

query_1 = """SELECT title,views FROM article_view LIMIT 3"""
query_2 = """SELECT authors.name,SUM(article_view.views) AS views FROM
article_view,authors WHERE authors.id = article_view.author
GROUP BY authors.name ORDER BY views DESC"""
query_3 = """SELECT * FROM error_log_view WHERE \"Percent Error\" > 1"""

def connect_db(query):
    db = psycopg2.connect("dbname=news")
    conn = db.cursor()
    conn.execute(query)
    results = conn.fetchall()
    conn.close()
    return results

if __name__ == "__main__":
  print("THE LIST OF POPULAR ARTICLES ARE:",connect_db(query_1))
  print("\n")
  print("THE LIST OF POPULAR AUTHORS ARE:",connect_db(query_2))
  print("\n")
  print("PERC ERROR MORE THAN 1.0:",connect_db(query_3))
