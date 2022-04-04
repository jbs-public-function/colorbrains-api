from typing import *


from .database import database_connection, compose_insert_sql, compose_select_sql
from .schemas import NamedColors, CategorizedColorMaps, ColorMaps


@database_connection
def insert_into_namedcolors(cursor, namedcolors_schema: NamedColors):
    query = compose_insert_sql("matplotlib", "namedcolors", list(namedcolors_schema.schema()['properties'].keys()))
    values = tuple(namedcolors_schema.color_name, namedcolors_schema.red, namedcolors_schema.green, namedcolors_schema.blue)
    return cursor.execute(query, (values, ))


@database_connection
def insertmany_into_namedcolors(cursor, namedcolors_schemas: List[NamedColors]):
    if len(namedcolors_schemas) <= 1:
        return insert_into_namedcolors(cursor, namedcolors_schemas[0])

    query = compose_insert_sql("matplotlib", "namedcolors", list(namedcolors_schemas[0].schema()['properties'].keys()))
    values = tuple([tuple(namedcolors_schema.color_name, namedcolors_schema.red, namedcolors_schema.green, namedcolors_schema.blue) for namedcolors_schema in namedcolors_schemas])
    
    return cursor.executemany(query, values)


@database_connection
def insert_into_categorizedcolormaps(cursor, categorized_colormap_meta: CategorizedColorMaps, colormaps: List[ColorMaps]):
    meta_query = compose_insert_sql("matplotlib", "categorizedcolormaps", list(categorized_colormap_meta.schema()['properties'].keys()))
    meta_values = tuple(categorized_colormap_meta.categorical_name, categorized_colormap_meta.colormap_name, categorized_colormap_meta.cmap_n_total)
    cursor.execute(meta_query, (meta_values, ))

    colormaps_query = compose_insert_sql("matplotlib", "colormaps", list(colormaps[0].schema()['properties'].keys()))


"""
-- create table for reference `color category` -> `colormap`
-- effectively labeled data
-- if a colormap has 22 colors `cmap_n_total` will be 22 
CREATE TABLE IF NOT EXISTS matplotlib.categorizedcolormaps (
    categorical_name TEXT NOT NULL,
    colormap_name TEXT UNIQUE NOT NULL,
    cmap_n_total INT NOT NULL,

    PRIMARY KEY  (categorical_name, colormap_name)
);


-- create table for colormaps
-- if a colormap has 22 colors `cmap_n_total` will be 22 
-- cmap_n_observation will be 1..22
-- references above table: matplotlib.categorizedcolormaps
CREATE TABLE IF NOT EXISTS matplotlib.colormaps (
    colormap_name TEXT NOT NULL,
    
    cmap_n_observation INT NOT NULL, 

    red FLOAT NOT NULL CHECK (red >= 0 AND red <=1),
    green FLOAT NOT NULL CHECK (green >= 0 AND green <=1),
    blue FLOAT NOT NULL CHECK (blue >= 0 AND blue <=1),
    
    PRIMARY KEY (colormap_name, cmap_n_observation),
    FOREIGN KEY (colormap_name) REFERENCES matplotlib.categorizedcolormaps (colormap_name)
);


-- create table for named colors
CREATE TABLE IF NOT EXISTS matplotlib.namedcolors (
    color_name TEXT NOT NULL PRIMARY KEY,
    red float NOT NULL CHECK (red >= 0 AND red <=1),
    green float NOT NULL CHECK (green >= 0 AND green <=1),
    blue float NOT NULL CHECK (blue >= 0 AND blue <=1)
);
"""