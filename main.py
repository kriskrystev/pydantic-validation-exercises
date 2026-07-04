
from models.product import Product


data = {
    "id": 1,
    "name": "Laptop",
    "sku": "ABC234",
    "price": 1000.0,
}

product = Product(**data)
