from fastapi import FastAPI
from app.server.routes.product import router as product_router

app = FastAPI(title="Random Shop")


app.include_router(product_router, tags=["Product"], prefix="/product")


@app.get("/", tags=["root_directory"])
async def hello_message():
    return {"message", "Hello. This is 'Random Shop'!"}
