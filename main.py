from fastapi import FastAPI
from db import db

app = FastAPI(title="Random Shop")


@app.get("/")
async def root():
    return {"app_name": "Random Shop"}


@app.get("/products")
async def products_list():
    products = await db["products"].find()
    return products
    