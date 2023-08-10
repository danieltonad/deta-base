from fastapi import FastAPI
from config.db import database
import uuid


app = FastAPI()


@app.get('/')
def index():
    resp = database.fetch()
    return resp
@app.get('/put')
def add():
    resp = database.insert(data={'message': 100}, key='test-me')
    return resp