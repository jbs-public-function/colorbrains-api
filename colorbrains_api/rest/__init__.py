from typing import *

from fastapi import FastAPI
from fastapi import Security

from .auth import get_api_key


app = FastAPI(
    title="Colorbrains Api",
    dependencies=Security(get_api_key)
)


@app.get('/')
def root():
    return {"status": "🌈"}