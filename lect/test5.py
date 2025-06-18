import unittest
from lab5 import MinValueDescriptor, Product

import pytest

class MinValueDescriptor:
    def __init__(self, min_value):
        self.min_value = min_value
        self.name = None
        def __set_name__(self, owner, name):
            self.name = name
        def __get__(self, instance, owner):
            return instance.__dict__.get(self.name, self.min_value)

    def __set__(self, instance, value):
        if value < self.min_value:
            raise ValueError(f"Значение должно быть не меньше {self.min_value}")
        instance.__dict__[self.name] = value

class Product:
    price = MinValueDescriptor(0)
    quantity = MinValueDescriptor(1)

    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

# Unit tests for Product and MinValueDescriptor
def test_product_initialization():
    p = Product(10, 5)
    assert p.price == 10
    assert p.quantity == 5

def test_product_initialization_with_min_values():
    p = Product(0, 1)
    assert p.price == 0
    assert p.quantity == 1

def test_product_price_below_min_value():
    with pytest.raises(ValueError, match=r"Значение должно быть не меньше 0"):
        Product(-1, 5)

def test_product_quantity_below_min_value():
    with pytest.raises(ValueError, match=r"Значение должно быть не меньше 1"):
        Product(10, 0)

def test_setting_price_to_below_min_value():
    p = Product(10, 5)
    with pytest.raises(ValueError, match=r"Значение должно быть не меньше 0"):
        p.price = -5

def test_setting_quantity_to_below_min_value():
    p = Product(10, 5)
    with pytest.raises(ValueError, match=r"Значение должно быть не меньше 1"):
        p.quantity = 0

def test_setting_valid_price():
    p = Product(10, 5)
    p.price = 15
    assert p.price == 15

def test_setting_valid_quantity():
    p = Product(10, 5)
    p.quantity = 10
    assert p.quantity == 10

def test_initial_descriptor_values():
    class TestClass:
        value = MinValueDescriptor(10)

    test_instance = TestClass()
    assert test_instance.value == 10
    test_instance.value = 15
    assert test_instance.value == 15

def test_initial_descriptor_values_below_default():
    class TestClass:
        value = MinValueDescriptor(10)

    test_instance = TestClass()
    with pytest.raises(ValueError, match=r"Значение должно быть не меньше 10"):
        test_instance.value = 5


if __name__ == '__main__':
    unittest.main()
