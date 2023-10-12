from pydantic import BaseModel, Field
from typing import Optional


class ProductSchema(BaseModel):
    product_id: str = Field(...)
    name: str = Field(...)
    color: str = Field(...)
    weight: float = Field(gt=0)
    brand: str = Field(...)

    class Config:
        schema_example = {
            "example": {
                "product_id": "Random id",
                "name": "Random product",
                "color": "Random color",
                "weight": "Random weight",
                "brand": "Random brand"
            }
        }


class UpdateProduct(BaseModel):
    product_id: Optional[str]
    name: str = Optional[str]
    color: str = Optional[str]
    weight: float = Optional[float]
    brand: str = Optional[str]

    class Config:
        schema_example = {
            "example": {
                "product_id": "77777777",
                "name": "Some product",
                "color": "Green",
                "weight": "777",
                "brand": "FunnyLucky"
            }
        }


def response_model(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def error_response_model(error, code, message):
    return {"error": error, "code": code, "message": message}
