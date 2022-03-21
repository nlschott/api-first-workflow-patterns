# reference - https://fastapi.tiangolo.com/#example
# 2022-03-16 NLS api-first-workflow-patterns
# fastapi python code first example
# to run this:
#  uvicorn main:app --reload

from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
