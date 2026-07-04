from pydantic import BaseModel, field_validator

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True
    tags: list[str] = []
    sku: str

    @field_validator("sku", mode="before")
    @classmethod
    def validate_sku(cls, value: str) -> str:
        if not value:
            raise ValueError("SKU is required.")
        if len(value) < 6:
            raise ValueError("SKU must be at least 6 characters long.")
        if len(value) > 7:
            raise ValueError("SKU must be at most 7 characters long.")
        if not value.isalnum():
            raise ValueError("SKU must be alphanumeric.")

        if len(value) == 7 and value[3] != "-":
            raise ValueError("SKU must be in the format 'XXX-XXX'.")
        
        if len(value) == 6:
            value = value[:3] + "-" + value[3:]

        return value.upper()

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str) -> str:
        value = value.strip()

        if not value:
            raise ValueError("Name is required.")
        
        if len(value) > 25:
            raise ValueError("Name must be at most 25 characters long.")
        return value

    @field_validator("price")
    @classmethod
    def validate_price(cls, value: float) -> float:
        if value <= 0:
            raise ValueError("Price must be greater than zero.")
        return value
