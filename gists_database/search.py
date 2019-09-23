from .models import Gist


def search_gists(db_connection, **kwargs):

    query = 'SELECT * FROM gists'

    if kwargs:
        query = build_query(kwargs.items())

    cursor = db_connection.execute(query)

    gists = [Gist(gist) for gist in cursor.fetchall()]

    return gists


def build_query(kwargs_items):

    OPERATORS = {'gt': '>',
                 'gte': '>=',
                 'lt': '<',
                 'lte': '<=',
                 'equal': '='
                 }

    query = 'SELECT * FROM gists'
    where_clause = ''
    operator = 'equal'
    conjunction = 'AND'

    for key, value in kwargs_items:

        if 'created_at' in key or 'updated_at' in key:
            value = value.strftime('%Y-%m-%dT%H:%M:%SZ')

            if len(key.rsplit('__')) > 1:
                operator = key.split('__')[-1]
                key = key.split('__')[0]

        where_clause += f" {conjunction} {key} {OPERATORS[operator]} '{value}'"

    where_clause = where_clause.replace('AND', 'WHERE', 1)

    return query + where_clause
