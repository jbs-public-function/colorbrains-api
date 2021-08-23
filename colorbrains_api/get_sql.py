import json
from colorbrains_api.db_assistant import DbAssistant
from psycopg2 import sql


def get_data(sql_statement):
    with DbAssistant().connection as conn:
        with conn.cursor() as cur:
            cur.execute(sql_statement)
            response = cur.fetchall()
            columns = [desc[0] for desc in cur.description]
    data = {'data': [dict(zip(columns, resp)) for resp in response]}
    return json.dumps(data)


def get_basecolors():
    sql_statement = """
        SELECT * FROM matplotlib.basecolors;
    """
    return get_data(sql_statement)


def get_categorized_colormaps():
    sql_statement = """
        SELECT * FROM matplotlib.categorizedcolormaps;
    """
    return get_data(sql_statement)


def get_colormaps():
    sql_statement = """
        SELECT * FROM matplotlib.colormaps;
    """
    return get_data(sql_statement)


def get_namedcolors():
    sql_statement = """
        SELECT * FROM matplotlib.namedcolors;
    """
    return get_data(sql_statement)