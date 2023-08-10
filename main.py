from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def index():
    print(100)