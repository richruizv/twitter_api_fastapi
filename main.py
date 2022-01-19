from models import User,Tweet

#fastapi
from fastapi import FastAPI



app = FastAPI()

@app.get(path="/")
def home():
    return {"Twitter API" : "Working!"}