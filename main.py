from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from mangum import Mangum
from open_ai import *

app = FastAPI()

if IS_LOCAL_ENV:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_methods=['*'],
        allow_headers=['*'],
    )    

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


class CoverLetterInfo(BaseModel):
    resume: str
    job_posting: str
    past_experiences: Union[str, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/completion/{prompt}")
def get_completion(prompt: str):
    result = text_completion(prompt)
    return result.choices[0].text


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


@app.post("/cover_letter")
def create_cover_letter(cover_letter_info: CoverLetterInfo):
    cover_letter = generate_cover_letter(cover_letter_info.resume, cover_letter_info.job_posting,
                                         cover_letter_info.past_experiences)
    return {"result" : cover_letter}

handler = Mangum(app)
