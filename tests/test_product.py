import pytest
from pydantic import ValidationError

from models.product import Product

def prepare_valid_data(**overrides):
    data = {"id": 1, "name": "Laptop", "sku": "ABC234", "price": 1000.0}
    data.update(overrides)
    return data

class TestProductNameValidation:
    def test_valid_product(self):
        p = Product(**prepare_valid_data())
        assert p.name == "Laptop"

    def test_name_too_short(self):
        with pytest.raises(ValidationError):
            Product(**prepare_valid_data(name=""))

    def test_name_too_long(self):
        with pytest.raises(ValidationError):
            Product(**prepare_valid_data(name="A" * 101))

class TestProductSkuValidation:
    def test_valid_product(self):
        p = Product(**prepare_valid_data())
        assert p.sku == "ABC-234"

    def test_sku_too_long(self):
        with pytest.raises(ValidationError):
            Product(**prepare_valid_data(sku="ABCDEFGHIJKL"))

    def test_sku_too_short(self):
        with pytest.raises(ValidationError):
            Product(**prepare_valid_data(sku="AB1"))

    def test_sku_invalid_characters(self):
        with pytest.raises(ValidationError):
            Product(**prepare_valid_data(sku="ABC%123"))

