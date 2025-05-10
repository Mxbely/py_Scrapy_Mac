def get_product_by_product_name(product_name, data):
    product = next(
        (product for product in data if product_name == product["name"]), None
    )
    return product
