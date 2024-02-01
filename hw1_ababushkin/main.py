from time import time
from typing import List, Dict

from fastapi import FastAPI
from pydantic import BaseModel

from logic import modify_data_to_human

import uvicorn


class ItemIn(BaseModel):
    params: Dict[str, List[Dict[str, int | str]]]


class ItemOut(BaseModel):
    params: str


app = FastAPI()


@app.get("/")
async def root():
    return f"opening hours of a restaurant"


@app.post("/items")
async def post_opening_hours(params: ItemIn):
    result = modify_data_to_human(params.params)
    return result


if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=8000)
