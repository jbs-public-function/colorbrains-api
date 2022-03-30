from typing import *

from fastapi import FastAPI
from fastapi import Security

from .auth import get_api_key
from .database import engine


app = FastAPI(
    title="Colorbrains Api",
    dependencies=[Security(get_api_key)]
)


@app.get('/')
def root():
    # health check
    return {"status": "🌈"}


@app.get('/test-create-engine')
def test_create_engine():
    engine
    return {"status": "🌈"}


@app.get('/another-test')
def another_test():
    try:
        with engine.connect():
            return {"status": "Connected!"}
    except Exception as exc:
        print(exc)
    return {'status': 'hi'}