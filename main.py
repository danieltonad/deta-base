from fastapi import FastAPI
from config.db import database
from schema.test_schema import test_serializer, tests_serializer
from model.test_model  import TestModel, TestRequest
import uuid

app = FastAPI()


@app.get('/')
async def index():
    resp = database.fetch()
    return resp

@app.post('/')
async def add(item: TestRequest):
    item.id = str(uuid.uuid1())
    resp = database.insert(data=dict(item), key=item.id)
    return resp

@app.get('/{key}')
async def find(key):
    resp = database.get(key)
    return resp

@app.post('/{key}')
async def update(item: TestModel, key : str):
    resp = database.put(dict(item), key=key)
    return resp
 