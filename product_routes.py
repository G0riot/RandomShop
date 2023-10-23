from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from db import (
    add_product,
    get_product,
    get_products,
    update_product,
    delete_product
)
from product_models import (
    response_model,
    ProductSchema,
    error_response_model,
    UpdateProduct
)

router = APIRouter()


@router.post("/", response_description="Product data added into the database")
async def add_product_data(product: ProductSchema = Body(...)):
    product = jsonable_encoder(product)
    new_student = await add_product(product)
    return response_model(new_student, "Student added successfully.")


@router.get("/", response_description="Products retrieved")
async def retrieved_products():
    products = await get_products()
    if products:
        return response_model(products, "Products data retrieved successfully")
    return response_model(products, "Empty list returned")


@router.get("/{id}", response_description="Product data retrieved")
async def get_product_data(id):
    product = await get_product(id)
    if product:
        return response_model(product, "Product data retrieved successfully")
    return error_response_model("An error occurred.", 404, "Product doesn't exist.")


@router.put("/{id}")
async def update_product_data(id: str, req: UpdateProduct = Body(...)):
    req = {k: v for k, v in req.model_dump().items() if v is not None}
    updated_product = await update_product(id, req)
    if updated_product:
        return response_model(
            "Product with ID: {} name update is successful".format(id),
            "Product name updated successfully",
        )
    return error_response_model(
        "An error occurred",
        404,
        "There was an error updating the product data.",
    )


@router.delete("/{id}", response_description="Product data deleted from the database")
async def delete_product_data(id: str):
    deleted_product = await delete_product(id)
    if deleted_product:
        return response_model(
            "Product with ID: {} removed".format(id), "Product deleted successfully"
        )
    return error_response_model(
        "An error occurred", 404, "Product with id {0} doesn't exist".format(id)
    )
