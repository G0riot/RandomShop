import motor.motor_asyncio as motor

url = "mongodb://localhost:27017/shopdb"

client = motor.AsyncIOMotorClient(url)
db = client.products