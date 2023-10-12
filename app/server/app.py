from fastapi import FastAPI

app = FastAPI(title="Random Shop")


@app.get("/", tags=["root_directory"])
async def hello_message():
    return {"message", "Hello. This is 'Random Shop'!"}
