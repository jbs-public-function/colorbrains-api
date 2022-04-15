from typing import *

from fastapi import FastAPI
from fastapi import Security

from .auth import get_api_key
from .models import insert_into_namedcolors, insert_into_categorizedcolormaps
from .schemas import NamedColors, CategorizedColorMaps, ManyNamedColors


app = FastAPI(
    title="Colorbrains Api",
    dependencies=[Security(get_api_key)]
)


@app.get('/')
def root():
    # health check
    return {"status": "🌈"}


@app.post('/matplotlib/named-colors/')
def insert_named_colors(named_colors: NamedColors):
    msg = insert_into_namedcolors(namedcolors_schemas=[named_colors])
    return {"status": "🌈"}


@app.post('/matplotlib/named-colors/many/')
def insert_many_named_colors(named_colors: ManyNamedColors):
    msg = insert_into_namedcolors(namedcolors_schemas=named_colors.named_colors)
    return {"status": "🌈"}


@app.post('/matplotlib/categorized-colormaps/')
def insert_named_categorized_colormaps(categorized_colormaps: CategorizedColorMaps):
    msg = insert_into_categorizedcolormaps(categorized_colormaps=categorized_colormaps)
    return {"status": "🌈"}
