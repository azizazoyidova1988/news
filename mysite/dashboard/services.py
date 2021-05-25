from django.db import connection
from contextlib import closing

def get_categories():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from dashboard_category""")
        categories=dict_fetchall(cursor)
        return categories

def get_categories_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select count(name) from dashboard_category""")
        categories=dict_fetchall(cursor)
        return categories

def get_categories_news_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT  count(dashboard_news.id),dashboard_category.name ,dashboard_news.category_id 
        FROM dashboard_category LEFT JOIN dashboard_news
		ON dashboard_news.category_id=dashboard_category.id
		GROUP BY dashboard_news.category_id,dashboard_category.name 
        ORDER BY COUNT(dashboard_news.id) DESC""")
        categories=dict_fetchall(cursor)
        return categories


def count_authors():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT COUNT(id), author_id  
        FROM dashboard_news
        GROUP BY author_id
        ORDER BY COUNT(id) DESC;""")
        categories=dict_fetchall(cursor)
        return categories

def get_authors():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from dashboard_author""")
        authors=dict_fetchall(cursor)
        return authors

def get_authors_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select count(full_name) from dashboard_author""")
        authors=dict_fetchall(cursor)
        return authors

def get_news():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from dashboard_news""")
        news=dict_fetchall(cursor)
        return news

def get_news_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select count(title) from dashboard_news""")
        news=dict_fetchall(cursor)
        return news

def get_references():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from dashboard_reference""")
        references=dict_fetchall(cursor)
        return references

def get_references_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select count(name) from dashboard_reference""")
        references=dict_fetchall(cursor)
        return references

def get_views():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select name, sum(views) as count from dashboard_category
        left join dashboard_news on dashboard_category.id=dashboard_news.category_id
        group by name""")
        views=dict_fetchall(cursor)
        return views


def dict_fetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def dict_fetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))