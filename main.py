from fastapi import FastAPI
from config.db import database
from schema.test_schema import test_serializer, tests_serializer
from model.test_model  import TestModel, TestRequest
import uuid

app = FastAPI()


@app.get('/')
async def index():
    resp = database.fetch()
    return tests_serializer(resp._items)

@app.post('/')
async def add(item: TestRequest):
    id = str(uuid.uuid1())
    resp = database.insert(data=dict(item), key=id)
    return resp

@app.get('/{id}')
async def find(id):
    resp = database.get(id)
    return resp

@app.post('/{id}')
async def update(item: TestRequest, id : str):
    resp = database.put(dict(item), key=id)
    return resp
 