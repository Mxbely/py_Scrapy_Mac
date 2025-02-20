from pydantic import BaseModel, ConfigDict


class ItemResponseSchema(BaseModel):
    name: str
    description: str
    calories: str
    fats: str
    carbs: str
    proteins: str
    unsaturated_fats: str
    sugar: str
    portion: str

    model_config = ConfigDict(from_attributes=True)


class PaginationResponseSchema(BaseModel):
    page: int
    size: int
    total: int
    total_pages: int
    data: list[ItemResponseSchema]

    model_config = ConfigDict(from_attributes=True)


class ItemFieldResponseSchema(BaseModel):
    product_field: str | int | float
