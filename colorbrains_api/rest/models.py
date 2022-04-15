from typing import *


from .database import database_connection, compose_insert_sql, compose_select_sql
from psycopg2.extras import execute_batch
from .schemas import CategorizedColorMapsMeta, NamedColors, CategorizedColorMaps, ColorMaps


def _insert_into_namedcolors(cursor, namedcolors_schema: NamedColors):
    schema_keys = list(namedcolors_schema.schema()['properties'].keys())
    query = compose_insert_sql(namedcolors_schema.schemaname, namedcolors_schema.tablename, schema_keys)
    values = tuple([getattr(namedcolors_schema, key) for key in schema_keys])
    cursor.execute(query, values)


@database_connection
def insert_into_namedcolors(cursor, namedcolors_schemas: List[NamedColors]):
    if len(namedcolors_schemas) <= 1:
        return _insert_into_namedcolors(cursor, namedcolors_schemas[0])

    schema_keys = list(namedcolors_schemas[0].schema()['properties'].keys())
    query = compose_insert_sql(namedcolors_schemas[0].schemaname, namedcolors_schemas[0].tablename, schema_keys)
    values = tuple([tuple([getattr(namedcolors_schema, key) for key in schema_keys]) for namedcolors_schema in namedcolors_schemas])
    
    execute_batch(cursor, query, values)


@database_connection
def insert_into_categorizedcolormaps(cursor, categorized_colormaps: CategorizedColorMaps):
    cmaps = categorized_colormaps.colormaps

    categorized_colormap_meta = CategorizedColorMapsMeta(
        categorical_name=categorized_colormaps.categorical_name,
        colormap_name=categorized_colormaps.colormap_name,
        cmap_n_total=len(cmaps)
    )

    colormaps = [ColorMaps(colormap_name=categorized_colormaps.colormap_name, red=cmap.red, blue=cmap.blue, green=cmap.green, cmap_n_observation=idx) for (idx, cmap) in enumerate(cmaps)]

    meta_schema_keys = list(categorized_colormap_meta.schema()['properties'].keys())
    meta_query = compose_insert_sql(categorized_colormap_meta.schemaname, categorized_colormap_meta.tablename, meta_schema_keys)
    meta_values = tuple([getattr(categorized_colormap_meta, key) for key in meta_schema_keys])
    cursor.execute(meta_query, meta_values)


    cmaps_schema_keys = list(colormaps[0].schema()['properties'].keys())
    colormaps_query = compose_insert_sql(colormaps[0].schemaname, colormaps[0].tablename, cmaps_schema_keys)
    colormaps_values = tuple([tuple([getattr(colormap, key) for key in cmaps_schema_keys]) for colormap in colormaps])

    execute_batch(cursor, colormaps_query, colormaps_values)
