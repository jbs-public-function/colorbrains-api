import csv
import io

from colorbrains_api.db_assistant import DbAssistant
from colorbrains_api.categorized_colormaps import MplCategorizedColormaps

from psycopg2 import sql
from matplotlib import colors
import matplotlib.pyplot as plt


def make_io_output(records):
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerows(records)
    output.seek(0)
    return output


def get_temp_table(table):
    return f'tmp_{table}'


def make_temp_table(schema, table):
    return sql.SQL("""
        CREATE TEMP TABLE {tmp_table} 
        (LIKE {schema}.{table} INCLUDING DEFAULTS)
        ON COMMIT DROP;
    """).format(
        tmp_table=sql.Identifier(get_temp_table(table)),
        schema=sql.Identifier(schema),
        table=sql.Identifier(table)
    )


def copy_from_temp_table(schema, table):
    return sql.SQL("""
        INSERT INTO {schema}.{table}
        SELECT *
        FROM {tmp_table}
        ON CONFLICT DO NOTHING;
    """).format(tmp_table=sql.Identifier(get_temp_table(table)),
        schema=sql.Identifier(schema),
        table=sql.Identifier(table)
    )


def populate_db(schema, table,  records):
    """
        Make Temp Table (On Commit Drop)
        Copy From io.StringIO Records To Temp Table
        Insert Into Table From Temp Table ON CONFLICT DO NOTHING
    """
    with DbAssistant().connection as conn:
        with conn.cursor() as cur:
            cur.execute(make_temp_table(schema, table))
            cur.copy_from(make_io_output(records), get_temp_table(table), sep=',')
            cur.execute(copy_from_temp_table(schema, table))
        conn.commit()


def make_basecolors_table():
    basecolor_records = []
    for color_name, (red, green, blue) in colors.BASE_COLORS.items():
        basecolor_records.append((color_name, red, green, blue))
    populate_db('matplotlib', 'basecolors', basecolor_records)


def make_categorized_colormaps_table():
    categorized_colormaps = []

    for cmap_category in MplCategorizedColormaps:
        for value in cmap_category.value:
            cmap = plt.get_cmap(value)
            categorized_colormaps.append(tuple([cmap_category.name, value, cmap.N]))
    populate_db('matplotlib', 'categorizedcolormaps', categorized_colormaps)


def get_colors(cmap):
    """
        Helper For make_colormaps_table()
    """
    if hasattr(cmap, 'colors'):
        return [color[:3] for color in cmap.colors]

    colors = []
    for i in range(cmap.N):
        colors.append(tuple([cmap(i)[0], cmap(i)[1], cmap(i)[2]]))
    return colors


def make_colormaps_table():
    colormaps = []
    for cmap_category in MplCategorizedColormaps:
        for cmap_name in cmap_category.value:
            cmap = plt.get_cmap(cmap_name)
            for n_obs, color in enumerate(get_colors(cmap)):
                red, green, blue = color[:3]
                colormaps.append(tuple([cmap.name, n_obs + 1, red, green, blue]))
    populate_db('matplotlib', 'colormaps', colormaps)


def make_namedcolors_table():
    namedcolors = []
    for cname, hexcolor in colors.cnames.items():
        namedcolors.append(tuple([cname] + list(colors.hex2color(hexcolor))))
    populate_db('matplotlib', 'namedcolors', namedcolors)


# Create Data
make_basecolors_table()
make_categorized_colormaps_table()
make_colormaps_table()
make_namedcolors_table()
