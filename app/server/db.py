import motor.motor_asyncio
from bson.objectid import ObjectId

url = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(url)
db = client.shopdb

products_collection = db.get_collection("products")


def product_helper(product) -> dict:
    return {
        "id": str(product["_id"]),
        "name": product["name"],
        "color": product["color"],
        "weight": product["weight"],
        "brand": product["brand"]
    }


async def get_products():
    products = []
    async for product in products_collection.find():
        products.append(product_helper(product))
    return products


async def add_product(product_data: dict) -> dict:
    product = await products_collection.insert_one(product_data)
    new_product = await products_collection.find_one({"_id": product.inserted_id})
    return product_helper(new_product)


async def get_product(id: str) -> dict:
    product = await products_collection.find_one({"_id": ObjectId(id)})
    if product:
        return product_helper(product)


async def update_product(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    product = await products_collection.find_one({"_id": ObjectId(id)})
    if product:
        updated_product = await products_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_product:
            return True
        return False


async def delete_product(id: str):
    product = await products_collection.find_one({"_id": ObjectId(id)})
    if product:
        await products_collection.delete_one({"_id": ObjectId(id)})
        return True
