from fastapi import FastAPI, Query, HTTPException
from api_server.utils import read_file
from api_server.crud import get_product_by_product_name
from api_server.schemas import (
    PaginationResponseSchema,
    ItemResponseSchema,
    ItemFieldResponseSchema,
)

app = FastAPI()


@app.get("/all_products/")
def get_all_products(page: int = Query(1, ge=1), size: int = Query(10, ge=1)):
    data = read_file()
    start = (page - 1) * size
    end = start + size
    paginated_data = data[start:end]

    return PaginationResponseSchema(
        **{
            "page": page,
            "size": size,
            "total": len(data),
            "total_pages": (len(data) + size - 1) // size,
            "data": paginated_data,
        }
    )


@app.get("/products/{product_name}")
def get_product_by_name(product_name: str):
    data = read_file()
    product = get_product_by_product_name(product_name, data)

    if not product:
        raise HTTPException(stasus_code=404, detail="Product not found")

    return ItemResponseSchema(**product)


@app.get("/products/{product_name}/{product_field}")
def get_product_field(product_name: str, product_field: str):
    data = read_file()
    product = get_product_by_product_name(product_name, data)

    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    if product_field not in product:
        raise HTTPException(status_code=404, detail="Field not found")

    return ItemFieldResponseSchema(product_field=product[product_field])
