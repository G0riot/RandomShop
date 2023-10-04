from fastapi import FastAPI
from db import db

app = FastAPI(title="Random Shop")

@app.get("/")
async def root():
    return {"app_name": app.title}