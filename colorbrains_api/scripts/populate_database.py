"""
@todo - fill out populate data scripts
"""

from colorbrains_api.db_assistant import DbAssistant

import psycopg2

# test code
# todo - replace with meaningfull populate data code

sql = ''' insert into matplotlib.basecolors(color_name, red, green, blue) VALUES ('xcolor', .35, .45, .55)'''
try:
    with DbAssistant().connection as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
        conn.commit()
except psycopg2.errors.UniqueViolation as err:
    print(err)
