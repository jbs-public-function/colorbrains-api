from fastapi import FastAPI

from colorbrains_api import get_sql


app = FastAPI()


@app.get("/basecolors")
def basecolors():
    return get_sql.get_basecolors()


@app.get("/categorized_colormaps")
def categorized_colormaps():
    return get_sql.get_categorized_colormaps()


@app.get("/colormaps")
def colormaps():
    return get_sql.get_colormaps()


@app.get("/namedcolors")
def namedcolors():
    return get_sql.get_namedcolors()
