from fastapi import FastAPI, Query, HTTPException
from api_server.utils import read_file


app = FastAPI()


@app.get("/all_products/")
def get_all_products(page: int = Query(1, ge=1), size: int = Query(10, ge=1)):
    data = read_file()
    start = (page - 1) * size
    end = start + size
    paginated_data = data[start:end]

    return {
        "page": page,
        "size": size,
        "total": len(data),
        "total_pages": (len(data) + size - 1) // size,  # Округлення вгору
        "data": paginated_data
    }


@app.get("/products/{product_name}")
def get_product_by_name(product_name: str):
    data = read_file()
    product = next(
        (product for product in data if product_name == product["name"]), 
        None
        )

    if product is None:
        raise HTTPException(
            stasus_code=404,
            detail="Product not found"
        )

    return product


@app.get("/products/{product_name}/{product_field}")
def get_product_field(product_name: str, product_field: str):
    data = read_file()
    product = next(
        (product for product in data if product_name == product["name"]), 
        None
        )

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    if not (value := product.get(product_field, None)):
        raise HTTPException(
            status_code=404,
            detail="Field not found"
        )

    return {product_field: value}
