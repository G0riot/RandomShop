from pydantic import BaseModel, Field


class ProductSchema(BaseModel):
    name: str = Field(...)
    color: str = Field(...)
    weight: float = Field(gt=0)
    brand: str = Field(...)

    class Config:
        schema_example = {
            "example": {
                "name": "Random product",
                "color": "Random color",
                "weight": "Random weight",
                "brand": "Random brand"
            }
        }