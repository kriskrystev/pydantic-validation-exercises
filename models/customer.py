from pydantic import BaseModel

from models.address import Address


class Customer(BaseModel):
    name: str
    address: Address
    shipping_address: Address | None = None