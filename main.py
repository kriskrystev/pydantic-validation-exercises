from datetime import date

from models.address import Address
from models.customer import Customer
from models.date_range import DateRange
from models.product import Product

product = Product(
    id=1,
    name="Laptop",
    sku="ABC234",
    price=1000.0,
    in_stock=True,
    tags=["electronics", "computers"],
)

billing_address = Address(
    street="123 Main St",
    city="Springfield",
    postal_code="12345",
)

shipping_address = Address(
    street="456 Oak Ave",
    city="Shelbyville",
    postal_code="67890",
)

customer = Customer(
    name="Jane Doe",
    address=billing_address,
    shipping_address=shipping_address,
)

sale_period = DateRange(
    start_date=date(2026, 7, 1),
    end_date=date(2026, 7, 31),
)

print(product)
print(customer)
print(sale_period)
