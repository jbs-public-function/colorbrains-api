import os
from typing import * 
import functools

import psycopg2
from psycopg2 import sql


def database_connection(func):
    @functools.wraps(func)
    def decorated(*args, **kwargs):
        with psycopg2.connect(os.environ["COLORBRAINS_CONN_STRING"]) as conn:
            cursor = conn.cursor()
            return func(cursor, *args, **kwargs)
    return decorated


def compose_insert_sql(
    schema: str,
    table: str,
    fields: List[str]
):
    return sql.SQL("INSERT INTO {table} ({fields}) VALUES ({values})").format(
        table=sql.Identifier(schema, table),
        fields=sql.SQL(', ').join(map(sql.Identifier, fields)),
        values=sql.SQL(', ').join(sql.Placeholder() * len(fields))
    )


def _compose_where_helper(sql_clause: str, clause_equivalency: str) -> psycopg2.sql.Composed:
    valid_equivalencys = ["=", "<", ">", "<=", ">=", "<>"]
    if clause_equivalency not in valid_equivalencys:
        raise Exception(f"Invalid clause_equivalency value given '{clause_equivalency}' not in '{valid_equivalencys}'")

    return sql.SQL(" {sql_clause}{clause_equivalency}{value} ").format(
        sql_clause=sql.Identifier(sql_clause),
        clause_equivalency=sql.SQL(clause_equivalency),
        value=sql.Placeholder()
    )


def _compose_where_statement(
    where_and_clause: List[Tuple[str, str]]=[],
    where_or_clause: List[Tuple[str, str]]=[]
) -> psycopg2.sql.Composed:

    composable_ands = None
    composable_ors = None

    _composable_ands = [_compose_where_helper(clause, equivalency) for (clause, equivalency) in where_and_clause]
    _composable_ors = [_compose_where_helper(clause, equivalency) for (clause, equivalency) in where_or_clause]

    if len(_composable_ands) > 0:
        composable_ands = sql.SQL(" AND ").join(_composable_ands)
    
    if len(_composable_ors) > 0:
        composable_ors = sql.SQL(" OR ").join(_composable_ors)

    if composable_ands is not None and composable_ors is not None:
        return sql.SQL(" WHERE ") + sql.SQL(" OR ").join([composable_ands, composable_ors])
    
    elif composable_ands is not None:
        return sql.SQL(" WHERE ") + composable_ands
    
    elif composable_ors is not None:
        return sql.SQL(" WHERE ") + composable_ors
    
    return sql.SQL("")


def compose_select_sql(
    schema: str,
    table: str,
    fields: List[str],
    where_and_clause: List[Tuple[str, str]]=[],
    where_or_clause: List[Tuple[str, str]]=[]
) -> psycopg2.sql.Composed:
    
    query = sql.SQL("SELECT {fields} FROM {table} ").format(
        table=sql.Identifier(schema, table),
        fields=sql.SQL(', ').join(map(sql.Identifier, fields)),
    )

    composable_where = _compose_where_statement(where_and_clause, where_or_clause)

    return query + composable_where
