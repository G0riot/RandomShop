import motor.motor_asyncio as motor

url = "mongodb://localhost:27017"

client = motor.AsyncIOMotorClient(url)
db = client.shopdb