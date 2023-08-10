from fastapi import FastAPI
from config.db import database
import uuid


app = FastAPI()


@app.get('/')
def index():
    resp = database.get()
    return resp
@app.get('/put')
def add():
    resp = database.put(data={'message': 100}, key=str(uuid.uuid1()))
    return resp