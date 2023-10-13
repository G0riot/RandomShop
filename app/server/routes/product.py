from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.db import (
    add_product,
    delete_product,
    get_products,
    get_products,
    update_product
)
from app.server.models.product import (
    error_response_model,
    response_model,
    ProductSchema,
    UpdateProduct,
)

router = APIRouter()


@router.post("/", response_description="Product data added into the database")
async def add_product_data(product: ProductSchema = Body(...)):
    product = jsonable_encoder(product)
    new_student = await add_product(product)
    return response_model(new_student, "Student added successfully.")
