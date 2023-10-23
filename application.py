from fastapi import FastAPI
from product_routes import router

app = FastAPI(title="Random Shop")


app.include_router(router, tags=["Product"], prefix="/product")


@app.get("/", tags=["Root"])
async def hello_message():
    return {"message", "Hello. This is 'Random Shop'!"}
