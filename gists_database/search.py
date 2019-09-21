from .models import Gist


def search_gists(db_connection, **kwargs):

    query = 'SELECT * FROM gists;'

    if kwargs:
        query = build_query(kwargs.items())

    cursor = db_connection.execute(query)

    gists = [Gist(gist) for gist in cursor.fetchall()]

    return gists


def build_query(kwargs_items):

    query = 'SELECT * FROM gists WHERE'

    where_clause = ''

    for key, value in kwargs_items:
        if key == 'created_at':
            value = format_created_at(value)

        where_clause += f" {key} = '{value}'"

    where_clause.replace(" ", " AND ")

    return query + where_clause


def format_created_at(datetime):
    return datetime.strftime('%Y-%m-%dT%H:%M:%SZ')

