from typing import Optional

from fastapi import FastAPI

from colorbrains_api.db_assistant import DbAssistant


app = FastAPI()

"""
@todo - flesh out endpoints
"""

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/read")
def read_root2():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
